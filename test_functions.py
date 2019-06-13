"""Test for Cell class in COGS18 S19 final project: Game of Life

elizabeth hostetter
A13091586
"""

from Life.py import Cell

def test_cell_class():

    '''
    test function for existence of Cell class object
    '''
    
    test_cell = Cell(True, 3, 2, 2)
    
    assert isinstance (test_cell, Cell)
    
    assert test_cell.life_state == True
   
    assert test_cell.live_neighbours == 3

    assert test_cell.xy_coord == 2