class Personagem():
    def __init__(self,nome,nivel,job,hp):
        self.nome = nome
        self.nivel = nivel
        self.job = job
        self.hp = hp

    def __str__(self):
        return f'Nome: {self.nome}\nNivel: {self.nivel}\nJob: {self.job}\nHP: {self.hp}'
        
"""
Força (Strength): Mede o poder físico e atlético.
Destreza (Dexterity): Mede a agilidade, reflexos e equilíbrio.
Constituição (Constitution): Representa a saúde e a resistência do personagem.
Inteligência (Intelligence): Refere-se à capacidade de raciocínio, memória 
e conhecimento.
Sabedoria (Wisdom): Mede a percepção, intuição e sintonia com o mundo.
Carisma (Charisma): Representa a força da personalidade, persuasão e liderança.

Características de Combate
Classe de Armadura (Armor Class - AC): Representa a defesa do personagem contra 
ataques.
Pontos de Vida (Hit Points - HP): Medem a vitalidade e a capacidade de um 
personagem de suportar dano.
Iniciativa (Initiative): Determina a ordem dos turnos em combate.
Bônus de Proficiência (Proficiency Bonus): É um bônus adicionado a rolagens nas 
quais o personagem é proficiente, como ataques com certas armas, perícias e 
testes de resistência.
Velocidade (Speed): A distância que um personagem pode se mover em um turno.

Outras Características Importantes
Raça (Race): A espécie do seu personagem (humano, elfo, anão, etc.), que
concede bônus de atributos e outras habilidades.
Classe (Class): A vocação do personagem (guerreiro, mago, ladino, etc.), que 
determina a maioria de suas habilidades.
Antecedente (Background): A história de origem do seu personagem, que concede 
proficiências em perícias e outros benefícios.
Alinhamento (Alignment): Descreve a bússola moral e a atitude do personagem 
(leal e bom, caótico e mau, etc.).
Perícias (Skills): Habilidades específicas como Atletismo, Furtividade, 
Arcanismo, entre outras, ligadas aos atributos principais.
Traços de Personalidade, Ideais, Vínculos e Defeitos: Detalhes que ajudam na 
interpretação do personagem.
"""