# Advent of Code 2020
# Day 20
# Author: irobin591

import os
import doctest
import re

re_tile_id = re.compile(r'^Tile ([0-9]+)\:$')

with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input_file:
    input_data = input_file.read().strip().split('\n\n')

class ImagePart():
    def from_input(data):
        data = data.split('\n')
        r = re_tile_id.match(data[0])
        if not r:
            raise RuntimeError("Invalid input (First line 'Tile XXXXX:' missing)")
        tile_id = int(r.group(1))
        return ImagePart(tile_id, [list(map(lambda x: x == '#', line)) for line in data[1:]])

    def __init__(self, tile_id, data):
        self.tile_id = tile_id
        self.data = data

        self.top_tile = None
        self.bottom_tile = None
        self.left_tile = None
        self.right_tile = None

    def rotate_part(self):
        # Rotates clockwise
        rotated = ImagePart(self.tile_id, self.data.copy())
        # https://stackoverflow.com/questions/8421337/rotating-a-two-dimensional-array-in-python
        rotated.data = [list(x) for x in zip(*rotated.data[::-1])]
        return rotated

    def flip_h_part(self):
        flipped = ImagePart(self.tile_id, self.data.copy())
        flipped.data = flipped.data[::-1]
        return flipped

    def flip_v_part(self):
        flipped = ImagePart(self.tile_id, self.data.copy())
        flipped.data = [x[::-1] for x in flipped.data]
        return flipped

    def get_top_border(self):
        return self.data[0]

    def get_bottom_border(self):
        return self.data[-1]

    def get_left_border(self):
        return [x[0] for x in self.data]

    def get_right_border(self):
        return [x[-1] for x in self.data]

    def possible_rotations_and_flips(self):
        x = self
        yield x
        yield x.flip_h_part()
        yield x.flip_v_part()
        yield x.flip_h_part().flip_v_part()
        for i in range(3):
            x = x.rotate_part()
            yield x
            yield x.flip_h_part()
            yield x.flip_v_part()
            yield x.flip_h_part().flip_v_part()

    @property
    def main_image(self):
        return [x[1:-1] for x in self.data[1:-1]]

    def __str__(self):
        s = "Tile {}:\n".format(self.tile_id)
        for line in self.data:
            s += ''.join(['#' if x else '.' for x in line])
            s += '\n'
        return s

    def __eq__(self, other):
        return self.tile_id == other.tile_id


def connect_neighbors(tile, pos, final_tiles):
    if not tile.top_tile:
        neighbor_pos = (pos[0], pos[1]+1)
        if neighbor_pos in final_tiles:
            related_tile = final_tiles[neighbor_pos]
            tile.top_tile = related_tile
            related_tile.bottom_tile = tile
            
    if not tile.bottom_tile:
        neighbor_pos = (pos[0], pos[1]-1)
        if neighbor_pos in final_tiles:
            related_tile = final_tiles[neighbor_pos]
            tile.bottom_tile = related_tile
            related_tile.top_tile = tile

    if not tile.left_tile:
        neighbor_pos = (pos[0]-1, pos[1])
        if neighbor_pos in final_tiles:
            related_tile = final_tiles[neighbor_pos]
            tile.left_tile = related_tile
            related_tile.right_tile = tile

    if not tile.right_tile:
        neighbor_pos = (pos[0]+1, pos[1])
        if neighbor_pos in final_tiles:
            related_tile = final_tiles[neighbor_pos]
            tile.right_tile = related_tile
            related_tile.left_tile = tile

def combine_tiles(tiles):
    """
    Glues ImageParts together
    """
    base_tiles = tiles.copy()

    # Select first tile as starting tile
    # tuple: (h, v)
    final_tiles = {(0,0): base_tiles.pop()}
    
    # Iterate until all tiles have been glued together
    while len(base_tiles) > 0:
        # Select a tile glued to the starting tile or the starting tile itself
        for tile_0_key in final_tiles.copy():
            tile_0 = final_tiles[tile_0_key]
            # Skip if a tile is already on each side
            if tile_0.top_tile and tile_0.bottom_tile and tile_0.left_tile and tile_0.right_tile:
                continue

            # Iterate though non glued tiles
            for tile_orig in base_tiles.copy():
                # In all possibilities: rotated and flipped
                for tile in tile_orig.possible_rotations_and_flips():
                    # Check if the rotated tile fits at the top border
                    if not tile_0.top_tile and tile_0.get_top_border() == tile.get_bottom_border():
                        # Only continue if both borders have not been glued to a tile
                        if not tile_0.top_tile and not tile.bottom_tile:
                            # Glue tiles together
                            tile_0.top_tile = tile
                            tile.bottom_tile = tile_0
                            
                            # Remove rotated tile from unglued tiless
                            base_tiles.remove(tile_orig)
                            
                            # Add to glued tiles
                            new_pos = (tile_0_key[0], tile_0_key[1]+1)
                            final_tiles[new_pos] = tile

                            # Connect borders to already glued tiles
                            #     O -- D
                            #     |    |
                            #     |    |
                            #     X ++ D
                            # O: tile_0
                            # X: Rotated tile
                            # D: Tiles already glued together
                            #
                            # +: Connection to be made with connect_neighbors
                            connect_neighbors(tile, new_pos, final_tiles)
                        break

                    # Check if the rotated tile fits at the bottom border
                    if not tile_0.bottom_tile and tile_0.get_bottom_border() == tile.get_top_border():
                        if not tile_0.bottom_tile and not tile.top_tile:
                            tile_0.bottom_tile = tile
                            tile.top_tile = tile_0
                            
                            base_tiles.remove(tile_orig)
                            
                            new_pos = (tile_0_key[0], tile_0_key[1]-1)
                            final_tiles[new_pos] = tile
                            connect_neighbors(tile, new_pos, final_tiles)
                        break

                    # Check if the rotated tile fits at the left border
                    if not tile_0.left_tile and tile_0.get_left_border() == tile.get_right_border():
                        if not tile_0.left_tile and not tile.right_tile:
                            tile_0.left_tile = tile
                            tile.right_tile = tile_0
                            
                            base_tiles.remove(tile_orig)

                            new_pos = (tile_0_key[0]-1, tile_0_key[1])
                            final_tiles[new_pos] = tile
                            connect_neighbors(tile, new_pos, final_tiles)
                        break

                    # Check if the rotated tile fits at the right border
                    if not tile_0.right_tile and tile_0.get_right_border() == tile.get_left_border():
                        if not tile_0.right_tile and not tile.left_tile:
                            tile_0.right_tile = tile
                            tile.left_tile = tile_0

                            base_tiles.remove(tile_orig)

                            new_pos = (tile_0_key[0]+1, tile_0_key[1])
                            final_tiles[new_pos] = tile
                            connect_neighbors(tile, new_pos, final_tiles)
                        break
    return final_tiles


def part1(input_data):
    """
    >>> part1(open(os.path.join(os.path.dirname(__file__), "test_part1.txt"), 'r').read().strip().split('\\n\\n'))
    20899048083289
    """

    tiles = []
    for tile in input_data:
        tiles.append(ImagePart.from_input(tile))

    final_tiles = combine_tiles(tiles)

    result = 1
    
    # get corner tiles
    for tile in final_tiles.values():
        if sum([bool(tile.top_tile), bool(tile.bottom_tile), bool(tile.left_tile), bool(tile.right_tile)]) == 2:
            result *= tile.tile_id
    return result


def part2(input_data):
    """
    >>> part2(open(os.path.join(os.path.dirname(__file__), "test_part1.txt"), 'r').read().strip().split('\\n\\n'))
    273
    """

    tiles = []
    for tile in input_data:
        tiles.append(ImagePart.from_input(tile))

    final_tiles = combine_tiles(tiles)

    # Combine ImageTiles to a bigger image

    # Search for top left tile
    top_left_tiles = list(filter(lambda t: not t.top_tile and not t.left_tile and t.right_tile and t.bottom_tile, final_tiles.values()))
    if len(top_left_tiles) != 1:
        raise RuntimeError("No or multiple tiles for the top left corner found")
    top_left_tile = top_left_tiles[0]

    complete_tile_data = []

    cur_tile_left = top_left_tile
    start_v = 0

    # Walk though image and add to complete_tile_data
    # row by row, starting from the left
    while cur_tile_left:
        cur_tile = cur_tile_left
        while cur_tile:
            for i, line in enumerate(cur_tile.main_image):
                if len(complete_tile_data) <= start_v+i:
                    complete_tile_data.append([])
                complete_tile_data[start_v+i].extend(line)
            
            cur_tile = cur_tile.right_tile
        start_v += len(cur_tile_left.main_image)
        cur_tile_left = cur_tile_left.bottom_tile

    complete_tile = ImagePart(0, complete_tile_data)

    # Regex for sea monster
    re_sea_monster1 = re.compile(r'^..................#.$')
    re_sea_monster2 = re.compile(r'^#....##....##....###$')
    re_sea_monster3 = re.compile(r'^.#..#..#..#..#..#...$')

    def bool_array_to_string(bool_array):
        return "".join(["#" if b else "." for b in bool_array])

    # get all rotation and flip variants
    for rotated_tile in complete_tile.possible_rotations_and_flips():
        # Search for sea monsters
        sea_monster_count = 0
        for h in range(0, len(rotated_tile.data)-2):
            for v in range(0, len(rotated_tile.data[0])-20):
                if (re_sea_monster1.match(bool_array_to_string(rotated_tile.data[h][v:v+20])) and
                    re_sea_monster2.match(bool_array_to_string(rotated_tile.data[h+1][v:v+20])) and
                    re_sea_monster3.match(bool_array_to_string(rotated_tile.data[h+2][v:v+20]))):
                    sea_monster_count += 1
        # if sea monster are found, substact the amount of sea monsters * 15 from the total amount of #s
        if sea_monster_count > 0:
            return sum([sum(line) for line in rotated_tile.data]) - (sea_monster_count * 15)
    
    raise RuntimeError("No sea monster found")


if __name__ == "__main__":
    doctest.testmod()
    print("Part One: {}".format(part1(input_data)))
    print("Part Two: {}".format(part2(input_data)))
    pass