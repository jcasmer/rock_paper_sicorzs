
import re
import random


class Game:
    '''
    juego para recordar como se juega piedra, papel, tijeras, lagarto, spock.
    '''

    # lista donde se observa que llave le gana a los elementos
    data_list = {
        'piedra': ['lagarto', 'tijeras'],
        'papel': ['piedra', 'spock'],
        'tijeras': ['papel', 'lagarto'],
        'lagarto': ['spock', 'papel'],
        'spock': ['tijeras', 'piedra']
    }

    def validate_option(self, player_choice):
        '''
        Método para validar las opciones ingresadas por los jugadores
        '''

        if not player_choice or player_choice not in self.data_list.keys():
            print('Valor ingresado no válido')
            return False
        return player_choice


    def get_winner(self, first_player, second_player):
        '''
        :param first_player: Opción elegida por el primer jugador
        :param second_player: Opción elegida por el segundo jugador
        :return: Booleano, Imprime el resultado
        '''

        if not self.validate_option(first_player) or not self.validate_option(second_player):
            return False

        if second_player in self.data_list[first_player]:
            print('Gana Jugador 1')
            return True

        if first_player in self.data_list[second_player]:
            print('Gana Jugador 2')
            return True

        if first_player == second_player:
            print('Empate')
            return True

    def one_vs_one(self):
        '''
        Método que se ejecuta cuando la opción elegida es 1 vs 1
        :return:
        '''
        flag = True
        first_player = None
        second_player = None
        while flag:
            if not first_player:
                first_player = self.validate_option(input(
                    'Jugador 1, ingrese una de las siguientes opciones (piedra, papel, tijeras, lagarto, spock) :'))
            if first_player and not second_player:
                second_player = self.validate_option(input(
                    'Jugador 2, ingrese una de las siguientes opciones (piedra, papel, tijeras, lagarto, spock) :'))
            if first_player and second_player:
                flag = False
        self.get_winner(first_player, second_player)
        return

    def one_vs_ia(self):
        '''
        Método que muestra el ganador entre el jugador y la máquina
        :return:
        '''
        flag = True
        first_player = None
        second_player = None
        while flag:
            if not first_player:
                first_player = self.validate_option(input(
                    'Jugador 1, ingrese una de las siguientes opciones (piedra, papel, tijeras, lagarto, spock) :'))
            if first_player:
                flag = False
        ia_player = random.choice(list(self.data_list.keys()))
        print('Opción elegida por la IA: ' + ia_player)
        self.get_winner(first_player, ia_player)
        return

    def menu(self):

        choice = input('Ingrese 1 para jugar 1 vs 1, ó 2 para 1 vs IA: ')
        if not re.match(r"^[1-2]+$", choice):
            print('Valor ingresado no válido.')
            self.menu()
        if choice == '1':
            self.one_vs_one()
        if choice == '2':
            self.one_vs_ia()


if __name__ == '__main__':
    app = Game()
    app.menu()

