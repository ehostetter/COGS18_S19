class Cell():
    '''
    create an object that lives or dies per the rules of Life
    
     1. Cell with less than 2 neighbours dies
     2. Cell with more than 3 neighbours dies
     3. Cell with 2 or 3 neighbours survives
     4. Cell with 3 neighbours is born
     
     
     ----PARAMETERS & VARIABLES----
     life_state = 0 or 1 
         dead or live 
         default = 0/dead
         
     live_neighbours = int 
         return from check_neighbours 
         default = 0
         
     symbol = int
         visual representation on grid
         default is dead state: "•" (8226)
         live state is "@" (64)
         
     method - check_neighbours: check for number of live neighbours
        there can be at most eight live neighbours - but no use checking after four are found
        
        neighbours = int: counter; 
            increase by one for every live neighbour found
            if/when neighbours =< 4, break loop
            
    created for COGS18 S19 final project
    elizabeth hostetter
    A13091586
    '''
    
    def __init__(self, life_state=False, live_neighbours=0, symbol=8226):

        self.life_state = life_state
        self.live_neighbours = live_neighbours
        self.symbol = chr(symbol) 
    
    def print_stats(self):
        '''
        for testing purposes to see if an object updates attributes correctly
        '''
            
        print(self.life_state, " ", self.symbol)