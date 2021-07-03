import json
import os
import shutil
import filecmp

from perlin_noise import PerlinNoise
import numpy as np
import matplotlib.pyplot as plt

from typing import Iterable

VERBOSITY_QUIET = 0
VERBOSITY_EXPLAIN = 1
VERBOSITY_ALL_OUTPUT = 2

SEED = 1

N_DECIMALS = 4

PATH_TO_SRC = os.path.dirname(os.path.realpath(__file__))
PATH_TO_LOG = os.path.join(PATH_TO_SRC, 'log')
PATH_TO_RESOURCEPACK = os.path.join(PATH_TO_SRC, 'resourcepack')
PATH_TO_DATAPACK = os.path.join(PATH_TO_SRC, 'datapack')
PATH_TO_MODELS = os.path.join(PATH_TO_RESOURCEPACK, 'assets/minecraft/models')


def printv(text, verbosity_needed=VERBOSITY_EXPLAIN, verbosity=VERBOSITY_EXPLAIN):
    if verbosity >= verbosity_needed:
        print(text)

# Creating animations -------------------------------------------------------


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
    with open(os.path.join(PATH_TO_MODELS, 'item/animation/{}/{}/frame_{}.json'.format(animation_name, middle_path, frame_id))) as frame_file:
        data = json.load(frame_file)
        for key in data['display'].keys():
            points[key] = np.array(data['display'][key]['rotation'] + data['display']
                                   [key]['translation'] + data['display'][key]['scale'])

    return points


def write_frame(point, animation_name, frame_id, model_parent='minecraft:item/handheld', key=False, verbosity=VERBOSITY_EXPLAIN):
    middle_path = 'output'
    if key:
        middle_path = 'key'
    with open(os.path.join(PATH_TO_MODELS, 'item/animation/{}/{}/frame_{}.json'.format(animation_name, middle_path, frame_id)), 'w+') as frame_file:
        data = {
            'parent': '{}'.format(model_parent), 'display': {}}
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
        printv('Writing json file for frame {}...'.format(
            frame_id), VERBOSITY_EXPLAIN, verbosity)
        printv(json.dumps(data, indent=2), VERBOSITY_ALL_OUTPUT, verbosity)
        json.dump(data, frame_file, indent=2)


def write_all_frames(start_point, animation_name, frame_offset, num_frames, path_func_dict, model_parent='minecraft:item/handheld', verbosity=VERBOSITY_EXPLAIN):
    for i in range(1, num_frames + 1):
        point_to_write = {}
        for point_of_view in start_point.keys():
            point_to_write[point_of_view] = path_func_dict[point_of_view](i)
        write_frame(point_to_write, animation_name,
                    frame_offset + i, model_parent=model_parent)


def create_animation_from_timeline(animation_name, overwrite=False, verbosity=VERBOSITY_EXPLAIN):
    if os.path.exists(os.path.join(PATH_TO_MODELS, 'item/animation/{}/output/build.json'.format(animation_name))):
        printv('Found build file for animation {}...'.format(
            animation_name), VERBOSITY_EXPLAIN, verbosity)
        #TODO: also check comparison with each key frame, not just timeline
        if filecmp.cmp(os.path.join(PATH_TO_MODELS, 'item/animation/{}/key/timeline.json'.format(animation_name)), os.path.join(PATH_TO_MODELS, 'item/animation/{}/output/build.json'.format(animation_name))):
            if not overwrite:
                printv('Timeline is unchanged for animation {}, skipping...'.format(
                    animation_name), VERBOSITY_EXPLAIN, verbosity)
                return
    seed = SEED
    printv('Removing {} output folder...'.format(
        animation_name), VERBOSITY_EXPLAIN, verbosity)
    try:
        shutil.rmtree(os.path.join(PATH_TO_MODELS,
                                   'item/animation/{}/output'.format(animation_name)))
    except:
        pass
    printv('Creating {} output folder...'.format(
        animation_name), VERBOSITY_EXPLAIN, verbosity)
    os.mkdir(os.path.join(PATH_TO_MODELS,
                          'item/animation/{}/output'.format(animation_name)))
    with open(os.path.join(PATH_TO_MODELS, 'item/animation/{}/key/timeline.json'.format(animation_name))) as timeline_file:
        timeline = json.load(timeline_file)
        model_parent = timeline['parent']
        offset = 0
        for section in timeline['sections']:
            if section['type'] == 'cubic':
                if (section['end_frame'] != 'generated') and (type(section['end_frame']) == int):
                    if section['start_frame'] == 'generated':
                        start_point = read_frame(
                            animation_name, 'generated', key=False)
                    else:
                        start_point = read_frame(
                            animation_name, section['start_frame'])
                    end_point = read_frame(
                        animation_name, section['end_frame'])

                    assert start_point.keys() == end_point.keys()
                    c9 = {}
                    for point_of_view in start_point.keys():
                        printv('Generating {} path over point of view {}...'.format(
                            section['type'], point_of_view), VERBOSITY_EXPLAIN, verbosity)
                        c9[point_of_view] = cubic_function_gen(
                            start_point[point_of_view], end_point[point_of_view], section['frames'])

                    write_all_frames(start_point, animation_name, offset,
                                     section['frames'], c9, model_parent, verbosity)
                else:
                    raise Exception(
                        'Cubic paths must have an end frame other than type \'generated\'.')
            elif section['type'] == 'perlin':
                if 'end_frame' not in section.keys():
                    start_point = read_frame(
                        animation_name, section['start_frame'])

                    n9 = {}
                    for point_of_view in start_point.keys():
                        printv('Generating {} path over point of view {}...'.format(
                            section['type'], point_of_view), VERBOSITY_EXPLAIN, verbosity)
                        n9[point_of_view] = perlin_function_gen(
                            start_point[point_of_view], section[point_of_view]['scales'], section[point_of_view]['wobble'], seed)

                    seed += 10  # just so there are no identical noises during a given animation

                    write_all_frames(start_point, animation_name, offset,
                                     section['frames'], n9, model_parent, verbosity)

                    shutil.copy(os.path.join(PATH_TO_MODELS, 'item/animation/{}/output/frame_{}.json'.format(animation_name, offset +
                                                                                                             section['frames'])), os.path.join(PATH_TO_MODELS, 'item/animation/{}/output/frame_generated.json'.format(animation_name)))
                else:
                    raise Exception(
                        'Perlin paths cannot include the key \'end_frame\'.')
            offset += section['frames']

    shutil.copy(os.path.join(PATH_TO_MODELS, 'item/animation/{}/key/timeline.json'.format(animation_name)),
                os.path.join(PATH_TO_MODELS, 'item/animation/{}/output/build.json'.format(animation_name)))

# Creating new filetree for new model -------------------------------------------------------


def write_model_file(name, layer0_name, num_frames, example_data, model_parent='minecraft:item/handheld', textured=True, verbosity=VERBOSITY_EXPLAIN):
    data = example_data.copy()
    data['parent'] = model_parent
    if textured:
        data['textures'] = {'layer0': '{}'.format(layer0_name)}
    data['overrides'] = []
    for i in range(num_frames):
        frame_json_obj = {'predicate': {'custom_model_data': i + 1},
                            'model': 'item/inspect/{}/frame_{}'.format(name, i + 1)}
        data['overrides'].append(frame_json_obj)

    # We want to open the file, read the contents, and append to it, not overwrite
    if os.path.exists(os.path.join(PATH_TO_MODELS, 'item/{}.json'.format(name))):
        with open(os.path.join(PATH_TO_MODELS, 'item/{}.json'.format(name))) as model_file:
            data_previous = json.load(model_file)
            # printv('{}.json exists, appending to it...'.format(
            #     name), VERBOSITY_EXPLAIN, verbosity)
            for key in data_previous.keys():
                if not (key in data.keys()):
                    data[key] = data_previous[key]
        # TODO: Implement this properly, currently we overwrite all contents. won't work for handheld for example, also uses texture not necessary
    printv('Writing base json file for item {}...'.format(
        name), VERBOSITY_EXPLAIN, verbosity)
    printv(json.dumps(data, indent=2), VERBOSITY_ALL_OUTPUT, verbosity)
    with open(os.path.join(PATH_TO_MODELS, 'item/{}.json'.format(name)), 'w+') as model_file:
        json.dump(data, model_file, indent=2)


def write_animation_folder(name, layer0_name, num_frames, animation_name='item_1', verbosity=VERBOSITY_EXPLAIN):
    printv('Removing inspect/{} folder...'.format(name),
           VERBOSITY_EXPLAIN, verbosity)
    try:
        shutil.rmtree(os.path.join(PATH_TO_MODELS,
                                   'item/inspect/{}'.format(name)))
    except:
        pass
    printv('Creating inspect/{} folder...'.format(name),
           VERBOSITY_EXPLAIN, verbosity)
    os.mkdir(os.path.join(PATH_TO_MODELS, 'item/inspect/{}'.format(name)))
    for i in range(num_frames):
        data = {'parent': 'minecraft:item/animation/{}/output/frame_{}'.format(animation_name, i + 1),
                'textures': {'layer0': '{}'.format(layer0_name)}}
        printv('Writing inspect/{}/frame_{}.json...'.format(name,
                                                            i + 1), VERBOSITY_EXPLAIN, verbosity)
        with open(os.path.join(PATH_TO_MODELS, 'item/inspect/{}/frame_{}.json'.format(name, i + 1)), 'w+') as frame_file:
            json.dump(data, frame_file, indent=2)


def write_model(name, layer0_name, example_data, model_parent='minecraft:item/handheld', textured=True, animation_name='item_1', verbosity=VERBOSITY_EXPLAIN):
    num_frames = len([name for name in os.listdir(os.path.join(
        PATH_TO_MODELS, 'item/animation/{}/output'.format(animation_name))) if name[6:-5].isnumeric()])

    if num_frames > 0:
        write_model_file(name, layer0_name, num_frames, example_data,
                         model_parent, textured, VERBOSITY_QUIET)
        write_animation_folder(name, layer0_name, num_frames,
                               animation_name, VERBOSITY_QUIET)
        printv('Creating animation {} for item {}...'.format(animation_name, name), VERBOSITY_EXPLAIN, verbosity)
    else:
        raise Exception('Number of frames must be greater than zero.')


# Creating key json of all items in version -------------------------------------------------------
def get_overview_of_models(path_to_dir, overwrite=False):
    if (overwrite == False) and (os.path.exists(os.path.join(PATH_TO_SRC, 'overview.json'))):
        return
    else:
        total_data = {}
        for model in os.listdir(path_to_dir):
            with open(os.path.join(path_to_dir, model)) as model_file:
                data = json.load(model_file)
                model_name = os.path.splitext(model)[0]
                total_data[model_name] = {}
                if 'parent' in data.keys():
                    total_data[model_name]['parent'] = data['parent']
                if 'textures' in data.keys():
                    if 'layer0' in data['textures'].keys():
                        total_data[model_name]['layer0'] = data['textures']['layer0']
                    # if data['parent'] not in total_data.keys():
                    #     total_data[data['parent']] = []
                    # total_data[data['parent']].append(
                    #     os.path.splitext(model)[0])

        with open(os.path.join(PATH_TO_SRC, 'overview.json'), 'w+') as overview_file:
            json.dump(total_data, overview_file, indent=2)


def load_overview_file():
    with open(os.path.join(PATH_TO_SRC, 'overview.json')) as overview_file:
        return json.load(overview_file)


def load_parents_file():
    with open(os.path.join(PATH_TO_SRC, 'parents.json')) as overview_file:
        return json.load(overview_file)

# Putting it all together -------------------------------------------------------------------------


def create_all_animations(overwrite=False, verbosity=VERBOSITY_EXPLAIN):
    get_overview_of_models(os.path.join(
        PATH_TO_MODELS, 'item/unused/items_21w07a'), overwrite=True)
    overview = load_overview_file()
    animation_names = [d for d in os.listdir(os.path.join(
        PATH_TO_MODELS, 'item/animation')) if os.path.isdir(os.path.join(PATH_TO_MODELS, 'item/animation/{}'.format(d)))]

    animation_pairing = {}
    for animation_name in animation_names:
        create_animation_from_timeline(animation_name, overwrite, verbosity)
        with open(os.path.join(PATH_TO_MODELS, 'item/animation/{}/key/timeline.json'.format(animation_name))) as timeline_file:
            timeline = json.load(timeline_file)
            animation_pairing[timeline['parent']] = animation_name
    
    printv('Opening example, constructing model file...',
        VERBOSITY_EXPLAIN, verbosity)
    example_data = {}
    with open(os.path.join(PATH_TO_SRC, 'example_item.json')) as example_file:
        example_data = json.load(example_file)
    
    for item in overview.keys():
        if ('parent' in overview[item].keys()) and ('parent' in overview[item].keys()):
            if overview[item]['parent'] in animation_pairing.keys():
                write_model(
                    item, overview[item]['layer0'], example_data, overview[item]['parent'], animation_name=animation_pairing[overview[item]['parent']])

# Miscellaneous utils -------------------------------------------------------------------------


def print_progress(fraction, width=25, empty_char=' ', fill_char='=', endcaps='[]', percent_after=True):
    progress = int(fraction * width)
    left = width - progress
    to_print = endcaps[0] + (progress * fill_char) + (left * empty_char) + endcaps[1]
    # if percent_after:
    #     to_print += ' {}%'.format(int(fraction * 100))
    print('\r' + to_print, end='')

if __name__ == "__main__": 
    create_all_animations(overwrite=True)
