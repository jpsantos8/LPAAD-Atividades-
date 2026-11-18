from musica import Musica

class Catalogo:
    def __init__(self):
        self.musicas = []
        self.musica_atual = None
        self.reproducoes = {}
        self.favoritos = []

    def adicionar_musica(self, musica):
        #validação para garantir que o objeto seja uma instância da classe Musica
        if not isinstance(musica, Musica):
            raise TypeError("É necessário fornecer um objeto da classe Musica.")
        self.musicas.append(musica)
        self.reproducoes[musica] = 0
        # chamar um método de favorito
        print(f"A música '{musica.nome}' foi adicionada ao catálogo de músicas.")

    def verificar_duplicidade():