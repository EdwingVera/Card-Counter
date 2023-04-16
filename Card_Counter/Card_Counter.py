import pynecone as pc

# Clase variables aplicación
class State(pc.State):
    
    # Inicializamos Conteo
    count : int = 0
    
    # Declaramos grupos de cartas
    low_cards = ("2", "3", "4", "5", "6")
    medium_cards = ("7", "8", "9")
    high_cards = ("10", "J", "Q", "K", "A")

    # Funcion conteo cartas
    def countCard(self, card : str):
        
        if card in self.low_cards:
            self.count += 1
        elif card in self.medium_cards:
            self.count = self.count
        elif card in self.high_cards:
            self.count -= 1
        else:
            print("Invalid Card")
            
    # Funcion reiniciar conteo
    def resetCounter(self):
        self.count = 0

# Funcion principal
def index() -> pc.Component:
    return pc.center(
        pc.box(
            pc.vstack(
                    # Contador                
                    pc.container(
                        pc.heading(State.count, size="xl", color="white"),
                        padding="10px",
                        center_content=True,
                        width="340px",
                        height="64px",
                        border_radius="8px",
                        bg="#3182CE",
                        ),
                    # Primera Columna Botones
                    pc.hstack(
                        pc.button("2", size="lg", width="100px", height="100px", color_scheme="blue", on_click=State.countCard("2")),
                        pc.button("3", size="lg", width="100px", height="100px", color_scheme="blue", on_click=State.countCard("3")),
                        pc.button("4", size="lg", width="100px", height="100px", color_scheme="blue", on_click=State.countCard("4")),
                        width="340px",
                        height="100px",
                        spacing="20px",
                        ),
                    # Primera Columna Botones
                    pc.hstack(
                        pc.button("5", size="lg", width="100px", height="100px", color_scheme="blue", on_click=State.countCard("5")),
                        pc.button("6", size="lg", width="100px", height="100px", color_scheme="blue", on_click=State.countCard("6")),
                        pc.button("7", size="lg", width="100px", height="100px", color_scheme="blue", on_click=State.countCard("7")),
                        width="340px",
                        height="100px",
                        spacing="20px",
                        ),
                    # Primera Columna Botones
                    pc.hstack(
                        pc.button("8", size="lg", width="100px", height="100px", color_scheme="blue", on_click=State.countCard("8")),
                        pc.button("9", size="lg", width="100px", height="100px", color_scheme="blue", on_click=State.countCard("9")),
                        pc.button("10", size="lg", width="100px", height="100px", color_scheme="blue", on_click=State.countCard("10")),
                        width="340px",
                        height="100px",
                        spacing="20px",
                        ),
                    # Primera Columna Botones
                    pc.hstack(
                        pc.button("J", size="lg", width="100px", height="100px", color_scheme="blue", on_click=State.countCard("J")),
                        pc.button("Q", size="lg", width="100px", height="100px", color_scheme="blue", on_click=State.countCard("Q")),
                        pc.button("K", size="lg", width="100px", height="100px", color_scheme="blue", on_click=State.countCard("K")),
                        width="340px",
                        height="100px",
                        spacing="20px",
                        ),
                    # Boton A
                    pc.button("A", size="lg", width="100px", height="100px", color_scheme="blue", on_click=State.countCard("A")),
                    width="100%",
                    spacing="25px",
                ),
            pc.button("Reiniciar", on_click=State.resetCounter),
            width="390px",
            height="787px",
            bg="#f0f0f0",
            border_radius="30px",
            padding="25px",
        ),
        padding_top="40px",
    )

# Agregamos State y Page a la App.
app = pc.App(state=State)
app.add_page(index)
app.compile()
