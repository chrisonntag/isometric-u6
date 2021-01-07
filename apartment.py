import os

from pygame import (K_DOWN, K_LEFT, K_RETURN,
                    K_RIGHT, K_SPACE, K_UP, K_l, K_x, K_z)

from isomyr.config import Keys
from isomyr.engine import Engine
from isomyr.objects.portal import Portal
from isomyr.objects.character import Player
from isomyr.skin import Skin, DirectedAnimatedSkin
from isomyr.util import ImageLoader
from isomyr.thing import MovableThing, PhysicalThing, PortableThing
from isomyr.universe import worldFactory, Universe

dirname = os.path.dirname(__file__)

# Set the custom keys for the game.
custom_keys = Keys(
    left=K_LEFT,
    right=K_RIGHT,
    up=K_UP,
    down=K_DOWN,
    jump=K_SPACE,
    pick_up=K_z,
    drop=K_x,
    examine=K_l,
    using=K_RETURN)


# An image loader that lets us run the tutorial anywhere the isomyr library
# can be imported (i.e., you don"t have to be in the same directory as the
# tutorial to run it).
image_loader = ImageLoader(dirname, transparency=(255, 255, 255))


def setupWorld():
    """
    Create the world, the scenes that can be visited, the objects in the
    scenes, and the player.
    """
    # Create the universe.
    universe = Universe(sceneSize=[842, 595])

    # Create the world.
    world = worldFactory(universe=universe, name="Game World", sceneSize=[842, 595])

    # Create the first scene.
    apartment = world.addScene("apartment")
    apartment.setSkin(
            Skin(image_loader.load("empty_u6.png")))

    # Create the player and set his animated skin.
    ian_curtis = apartment.addPlayer(
        name="Ian Curtis", location=[20, 20, 0], size=[14, 14, 50],
        velocityModifier=2)
    south_facing = image_loader.load([
        "player/ian_curtis1.png", "player/ian_curtis2.png",
        "player/ian_curtis3.png"])
    east_facing = image_loader.load([
        "player/ian_curtis4.png", "player/ian_curtis5.png",
        "player/ian_curtis6.png"])
    ian_curtis.setSkin(
        DirectedAnimatedSkin(south_facing, east_facing,
                             frameSequence=[0, 2, 2, 1, 1, 2, 2, 0]))

    # Create NPC
    jonas = Player(
        name="Jonas", location=[20, 120, 0], size=[14, 14, 50],
        velocityModifier=2)
    south_facing = image_loader.load([
        "player/ian_curtis1.png", "player/ian_curtis2.png",
        "player/ian_curtis3.png"])
    east_facing = image_loader.load([
        "player/ian_curtis4.png", "player/ian_curtis5.png",
        "player/ian_curtis6.png"])
    jonas.setSkin(
        DirectedAnimatedSkin(south_facing, east_facing,
                             frameSequence=[0, 2, 2, 1, 1, 2, 2, 0]))


    ground = PhysicalThing(
        "ground", [-2000, -1000, -100], [4000, 2000, 100])
    outer_long_wall = PhysicalThing("wall", [0, 0, -20], [20, 680, 120])
    outer_short_wall = PhysicalThing("wall", [0, -10, -20], [300, 20, 120])
    inner_long_wall = PhysicalThing("wall", [200, 0, -20], [20, 680, 120])
    inner_short_wall = PhysicalThing("wall", [0, 580, -20], [300, 20, 120])

    # Populate walls, ground and add NPC
    apartment.addObjects([
        ground, outer_long_wall, outer_short_wall, inner_long_wall, inner_short_wall, jonas])

    # Add items
    bed_chris = PhysicalThing(
        name="bed_chris", location=[5, 10, 0], size=[39, 66, 37], fixed=False)
    bed_chris.setSkin(
        Skin(image_loader.load(["items/u6_0012_bed_big_r.png"])))

    apartment.addObjects([
        bed_chris
        ])
    

    return world


def run():
    # Setup the pygame display, the window caption and its icon.
    world = setupWorld()
    # Create an isomyr engine and start it.
    engine = Engine(world=world, offset=[590, 127], keys=custom_keys, titleFile=os.path.join(dirname, 'titlebar.png'))
    engine.start()

    print engine.universe.getPlayer().location


if __name__ == "__main__":
    run()
