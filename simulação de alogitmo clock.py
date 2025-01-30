class ClockAlgorithm:
    def __init__(self, num_frames):
        self.num_frames = num_frames  # Quantidade de quadros disponíveis
        self.frames = [-1] * num_frames  # Inicializa os quadros vazios
        self.ref_bits = [0] * num_frames  # Bits de referência
        self.pointer = 0  # Ponteiro

    def access_page(self, page):
        page_fault = False

        if page in self.frames:  # Se a página já estiver na memória
            index = self.frames.index(page)
            self.ref_bits[index] = 1  # Define o bit de referência como 1
        else:
            page_fault = True  # Ocorre um Page Fault
            while True:
                if self.ref_bits[self.pointer] == 0:  # Se o bit for 0, substitui a página
                    self.frames[self.pointer] = page
                    self.ref_bits[self.pointer] = 1
                    self.pointer = (self.pointer + 1) % self.num_frames  # Move o ponteiro
                    break
                else:  # Se o bit for 1, reseta e move o ponteiro
                    self.ref_bits[self.pointer] = 0
                    self.pointer = (self.pointer + 1) % self.num_frames

        # Formata e imprime os dados da tabela
        frames_state = [f"{f}" if f != -1 else "-" for f in self.frames]
        bits_state = [str(b) for b in self.ref_bits]
        print(f"{page:<8} {frames_state} {bits_state} {'Sim' if page_fault else 'Não'}")

    def run_simulation(self, access_sequence):
        print("\nSimulação do Algoritmo Clock\n")
        print(f"{'Acesso':<8} {'Ordem dos Frames':<20} {'Ordem dos Bits':<20} Page Fault")
        print("=" * 60)
        for page in access_sequence:
            self.access_page(page)

# Entrada do usuário
num_frames = int(input("Digite o número de frames: "))
access_sequence = list(map(int, input("Digite a sequência de acessos separados por espaço: ").split()))

# Inicializa e roda a simulação
clock_simulator = ClockAlgorithm(num_frames)
clock_simulator.run_simulation(access_sequence)
