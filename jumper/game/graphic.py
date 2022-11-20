class Graphic:
    def __init__(self):
        self._graphic = 0
        self._graphic = 0


    def print_parachute(self, lives):
        decrease_lives = [  
            """
             x 
            /|\ 
            / \ 
       ^^^^^^^^^^^^^
            """,

            """
            \ /
             O
            /|\ 
            / \ 
       ^^^^^^^^^^^^^
            """,

            """
           \   /
            \ /
             O
            /|\ 
            / \ 
       ^^^^^^^^^^^^^
            """,

            """
          \     /
           \   /
            \ /
             O
            /|\ 
            / \ 
       ^^^^^^^^^^^^^
            """,
            
            """     
          /_____\ 
          \     /
           \   /
            \ /
             O
            /|\ 
            / \ 
       ^^^^^^^^^^^^^
            """,
        
            """
           _____
          /_____\ 
          \     /
           \   /
            \ /
             O
            /|\ 
            / \ 
       ^^^^^^^^^^^^^
            """,
            ]
        return print(decrease_lives[lives])