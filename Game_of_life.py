#! /usr/bin/env python3

import time

class board():
    """
        La clase board contiene el tablero como una matriz NxN.
        Cada elemento es una célula: si está viva, guarda un 1; si está muerta, un 0
    """
    def __init__(self, rows, columns, initial_cells):
        """
            Al crearse, se necesita el numero de filas y columnas y las celulas vivas iniciales.
            rows -> Numero de filas (int)
            columns -> Numero de columnas (int)
            initial_cells -> celulas vivas (tupla de tuplas con dos elementos X e Y (int, int))
        """
        # Creamos el tablero vacío y lo llenamos con ceros (muertos)
        self.rows, self.columns = rows, columns
        self.board = self._create_empty_board(rows, columns)
        # Cambiamos el estado inicial a vivo de las células indicadas
        # Cada elemento de initial_cells es una tupla de dos elementos con X e Y
        for cell in initial_cells:
            row = cell[0]
            column = cell[1]
            self.board[row][column] = 1

    def _create_empty_board(self, rows, columns):
        """
            El tablero vacio es la matriz NxN con 0 en todas las posiciones
        """
        board = []
        for i in range(rows):
            row = []
            for j in range(columns):
                row.append(0)
            board.append(row)
        return board

    def _check_neighbours(self, cell):
        """
            Comprueba el numero de vecinos que están vivos. Necesita una celda con las coordenadas de la celula
            cell -> Tupla de dos elementos X e Y (int, int)
        """
        row = cell[0]
        column = cell[1]
        alive = 0
        prev_column = column-1
        next_column = column+1
        # Celdas superiores
        if (row-1 >= 0):
            # Celda Superior izquierda
            if (prev_column >= 0 and self.board[row-1][prev_column]):
                alive+=1
            # Celda superior central
            if (self.board[row-1][column] == 1):
                alive+=1
            # Celda superior derecha
            if (next_column < self.columns and self.board[row-1][next_column]):
                alive+=1
        # Fila central
        # Celda izquierda
        if (prev_column >= 0 and self.board[row][prev_column]):
            alive += 1
        # Celda a la derecha
        if (next_column < self.columns and self.board[row][next_column]):
            alive += 1
        # Fila infierior
        if (row + 1 < self.rows):
            # Celda inferior izquierda
            if (prev_column >= 0 and self.board[row+1][prev_column]):
                alive += 1
            # Celda inferior central
            if (self.board[row+1][column]):
                alive += 1
            # Celda inferior derecha
            if (next_column < self.columns and self.board[row+1][next_column]):
                alive += 1
        return alive

    def _is_over(self):
        """
            Comprueba si todas las células están muertas, ya que si es el caso,
            no hay mas iteraciones.
        """
        for i in range(self.rows):
            for j in range(self.columns):
                if (self.board[i][j] != 0):
                    return False
        return True


    # Calcula la nueva iteracion del tablero
    def next_iteration(self):
        """
            Calcula la siguiente iteración del juego
        """
        new_board = self._create_empty_board(self.rows, self.columns)
        # Para cada célula, comprueba los vecinos vivos y decide si sigue viva o muerta
        for i in range(self.rows):
            for j in range(self.columns):
                alive = self._check_neighbours((i, j))
                # Si tiene 3 vecinos, esté viva o muerta, en la siguiente gen está viva
                if (alive == 3):
                    new_board[i][j] = 1
                # Si tiene 2 vecinos Y está viva, sigue viva
                elif (alive == 2 and self.board[i][j] == 1):
                    new_board[i][j] = 1
                # En cualquier otro caso, muerte
                else:
                    new_board[i][j] = 0
        self.board = new_board
        pass

    def _print(self, i):
        """
        Imprime el juego en pantalla
        """
        print ("Iteración "+str(i))
        for row in self.board:
            for cell in row:
                print("*\t", end="") if cell == 1 else print("\t", end="")
            print("")
        print()


if __name__ == "__main__":
    b = board(3, 3, [(1,1), (0, 1), (2, 1)])
    i = 0
    while(not b._is_over()):
        b._print(i)
        b.next_iteration()
        i+= 1
        time.sleep(1)
