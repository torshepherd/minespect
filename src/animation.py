from typing import Iterable
import numpy as np
import matplotlib.pyplot as plt
import json
from perlin_noise import PerlinNoise
import os
import shutil

VERBOSITY_QUIET = 0
VERBOSITY_EXPLAIN = 1
VERBOSITY_ALL_OUTPUT = 2

SEED = 1

N_DECIMALS = 4

PATH_TO_MODELS = os.path.join(os.getcwd(), 'assets/minecraft/models')

def printv(text, verbosity_needed=VERBOSITY_EXPLAIN, verbosity=VERBOSITY_EXPLAIN):
    if verbosity >= verbosity_needed:
        print(text)


def cubic_function_gen(start_point, end_point, frames: int):
    # cubic(t)           => c1(t)**3 + c2(t)**2 + c3t + c4
    # start_point at t=0 => c4 = start_point
    # first derivative   => 3c1(t)**2 + 2c2t + c3
    # zero at t=0        => c3 = 0
    # zero at t=frames   => c2 = -1.5c1(frames)

    # cubic(t)              => c1(t)**3 - 1.5c1(frames)(t)**2 + start_point
    # end_point at t=frames => c1 = -2 (end_point - start_point) / (frames)**3

    c1 = -2 * (end_point - start_point) / ((frames)**3)
    c2 = -1.5 * c1 * (frames)
    c3 = 0
    c4 = start_point

    return lambda t: c1 * (t**3) + c2 * (t**2) + c3 * t + c4


def perlin_function_gen(start_point, scales: Iterable, wobblinesses: Iterable, seed: int):
    """
    Takes in start_point, scales, and wobbliness (np.array, shape=(n,)) 
    """
    
    noises = []
    for i in range(start_point.shape[0]):
        noises.append(PerlinNoise(wobblinesses[i], seed + i))
    
    return lambda t: np.array([start_point[i] + scales[i] * noises[i](t / 25) for i in range(start_point.shape[0])])

# Frame I/O


def read_frame(animation_name, frame_id, key=True):
    middle_path = 'output'
    if key:
        middle_path = 'key'
    points = {}
    with open(os.path.join(PATH_TO_MODELS, 'item/{}/{}/frame_{}.json'.format(animation_name, middle_path, frame_id))) as frame_file:
        data = json.load(frame_file)
        for key in data['display'].keys():
            points[key] = np.array(data['display'][key]['rotation'] + data['display']
                                   [key]['translation'] + data['display'][key]['scale'])

    return points


def write_frame(point, animation_name, frame_id, model_parent='handheld', key=False, verbosity=VERBOSITY_EXPLAIN):
    middle_path = 'output'
    if key:
        middle_path = 'key'
    with open(os.path.join(PATH_TO_MODELS, 'item/{}/{}/frame_{}.json'.format(animation_name, middle_path, frame_id)), 'w+') as frame_file:
        data = {
            'parent': 'minecraft:item/{}'.format(model_parent), 'display': {}}
        if 'firstperson_righthand' in point.keys():
            data['display']['firstperson_righthand'] = {'rotation': list(point['firstperson_righthand'][:3].round(N_DECIMALS)),
                                                        'translation': list(point['firstperson_righthand'][3:6].round(N_DECIMALS)),
                                                        'scale': list(point['firstperson_righthand'][6:].round(N_DECIMALS))}
        if 'thirdperson_righthand' in point.keys():
            data['display']['thirdperson_righthand'] = {'rotation': list(point['thirdperson_righthand'][:3].round(N_DECIMALS)),
                                                        'translation': list(point['thirdperson_righthand'][3:6].round(N_DECIMALS)),
                                                        'scale': list(point['thirdperson_righthand'][6:].round(N_DECIMALS))}
        if 'firstperson_lefthand' in point.keys():
            data['display']['firstperson_lefthand'] = {'rotation': list(point['firstperson_lefthand'][:3].round(N_DECIMALS)),
                                                       'translation': list(point['firstperson_lefthand'][3:6].round(N_DECIMALS)),
                                                       'scale': list(point['firstperson_lefthand'][6:].round(N_DECIMALS))}
        if 'thirdperson_lefthand' in point.keys():
            data['display']['thirdperson_lefthand'] = {'rotation': list(point['thirdperson_lefthand'][:3].round(N_DECIMALS)),
                                                       'translation': list(point['thirdperson_lefthand'][3:6].round(N_DECIMALS)),
                                                       'scale': list(point['thirdperson_lefthand'][6:].round(N_DECIMALS))}
        printv('Writing json file for frame {}...'.format(frame_id), VERBOSITY_EXPLAIN, verbosity)
        printv(json.dumps(data, indent=2), VERBOSITY_ALL_OUTPUT, verbosity)
        json.dump(data, frame_file, indent=2)
        
def write_all_frames(start_point, animation_name, frame_offset, num_frames, path_func_dict, model_parent='handheld', verbosity=VERBOSITY_EXPLAIN):
    for i in range(1, num_frames + 1):
        point_to_write = {}
        for point_of_view in start_point.keys():
            point_to_write[point_of_view] = path_func_dict[point_of_view](i)
        write_frame(point_to_write, animation_name, frame_offset + i, model_parent=model_parent)

def create_animation_from_timeline(animation_name, model_parent='handheld', verbosity=VERBOSITY_EXPLAIN):
    seed = SEED
    printv('Removing {} output folder...'.format(animation_name), VERBOSITY_EXPLAIN, verbosity)
    try:
        shutil.rmtree(os.path.join(PATH_TO_MODELS, 'item/{}/output'.format(animation_name)))
    except:
        pass
    printv('Creating {} output folder...'.format(animation_name), VERBOSITY_EXPLAIN, verbosity)
    os.mkdir(os.path.join(PATH_TO_MODELS, 'item/{}/output'.format(animation_name)))
    with open(os.path.join(PATH_TO_MODELS, 'item/{}/key/timeline.json'.format(animation_name))) as timeline_file:
        timeline = json.load(timeline_file)
        offset = 0
        for section in timeline['sections']:
            if section['type'] == 'cubic':
                if (section['end_frame'] != 'generated') and (type(section['end_frame']) == int):
                    start_point = read_frame(animation_name, section['start_frame'])
                    end_point = read_frame(animation_name, section['end_frame'])
                    
                    assert start_point.keys() == end_point.keys()
                    c9 = {}
                    for point_of_view in start_point.keys():
                        printv('Generating {} path over point of view {}...'.format(section['type'], point_of_view), VERBOSITY_EXPLAIN, verbosity)
                        c9[point_of_view] = cubic_function_gen(start_point[point_of_view], end_point[point_of_view], section['frames'])

                    write_all_frames(start_point, animation_name, offset, section['frames'], c9, model_parent, verbosity)
                else:
                    raise Exception('Cubic paths must have an end frame other than type \'generated\'.')
            elif section['type'] == 'perlin':
                if 'end_frame' not in section.keys():
                    start_point = read_frame(animation_name, section['start_frame'])
                    
                    n9 = {}
                    for point_of_view in start_point.keys():
                        printv('Generating {} path over point of view {}...'.format(section['type'], point_of_view), VERBOSITY_EXPLAIN, verbosity)
                        n9[point_of_view] = perlin_function_gen(start_point[point_of_view], section[point_of_view]['scales'], section[point_of_view]['wobble'], seed)

                    seed += 10 # just so there are no identical noises during a given animation

                    write_all_frames(start_point, animation_name, offset, section['frames'], n9, model_parent, verbosity)

                    shutil.copy(os.path.join(PATH_TO_MODELS, 'item/{}/output/frame_{}.json'.format(animation_name, offset + section['frames'])), os.path.join(PATH_TO_MODELS, 'item/{}/key/frame_generated.json'.format(animation_name)))
                else:
                    raise Exception('Perlin paths cannot include the key \'end_frame\'.')
            offset += section['frames']

# Creating new filetree for new model


def write_model_file(name, num_frames, model_parent='handheld', textured=True, verbosity=VERBOSITY_EXPLAIN):
    printv('Opening example, constructing model file...', VERBOSITY_EXPLAIN, verbosity)
    with open('example_item.json') as example_file:
        data = json.load(example_file)

        data['parent'] += model_parent
        if textured:
            data['textures'] = {'layer0': 'minecraft:item/{}'.format(name)}
        data['overrides'] = []
        for i in range(num_frames):
            frame_json_obj = {'predicate': {'custom_model_data': i + 1},
                              'model': 'item/inspect_{}/frame_{}'.format(name, i + 1)}
            data['overrides'].append(frame_json_obj)

        # We want to open the file, read the contents, and append to it, not overwrite
        if os.path.exists(os.path.join(PATH_TO_MODELS, 'item/{}.json'.format(name))):
            with open(os.path.join(PATH_TO_MODELS, 'item/{}.json'.format(name))) as model_file:
                data_previous = json.load(model_file)
                printv('{}.json exists, appending to it...'.format(name), VERBOSITY_EXPLAIN, verbosity)
                for key in data_previous.keys():
                    if not (key in data.keys()):
                        data[key] = data_previous[key]
            # TODO: Implement this properly, currently we overwrite all contents. won't work for handheld for example, also uses texture not necessary
        printv('Writing base json file for item {}...'.format(name), VERBOSITY_EXPLAIN, verbosity)
        printv(json.dumps(data, indent=2), VERBOSITY_ALL_OUTPUT, verbosity)
        with open(os.path.join(PATH_TO_MODELS, 'item/{}.json'.format(name)), 'w+') as model_file:
            json.dump(data, model_file, indent=2)


def write_animation_folder(name, num_frames, animation_name='sword_animation_1', verbosity=VERBOSITY_EXPLAIN):
    printv('Removing inspect_{} folder...'.format(name), VERBOSITY_EXPLAIN, verbosity)
    try:
        shutil.rmtree(os.path.join(PATH_TO_MODELS, 'item/inspect_{}'.format(name)))
    except:
        pass
    printv('Creating inspect_{} folder...'.format(name), VERBOSITY_EXPLAIN, verbosity)
    os.mkdir(os.path.join(PATH_TO_MODELS, 'item/inspect_{}'.format(name)))
    for i in range(num_frames):
        data = {'parent': 'minecraft:item/{}/output/frame_{}'.format(animation_name, i + 1),
                'textures': {'layer0': 'minecraft:item/{}'.format(name)}}
        printv('Writing inspect_{}/frame_{}.json...'.format(name, i + 1), VERBOSITY_EXPLAIN, verbosity)
        with open(os.path.join(PATH_TO_MODELS, 'item/inspect_{}/frame_{}.json'.format(name, i + 1)), 'w+') as frame_file:
            json.dump(data, frame_file, indent=2)


def write_model(name, model_parent='handheld', textured=True, animation_name='sword_animation_1', verbosity=VERBOSITY_EXPLAIN):
    num_frames = len([name for name in os.listdir(os.path.join(PATH_TO_MODELS, 'item/{}/output'.format(animation_name)))])
    
    if num_frames > 0:
        write_model_file(name, num_frames, model_parent, textured, verbosity)
        write_animation_folder(name, num_frames, animation_name, verbosity)
    else:
        raise Exception('Number of frames must be greater than zero.')

# Open input frame json file
# Open output frame json file
# Generate cubic function mapping between them
# Iterate over frames, generating each frame json file
