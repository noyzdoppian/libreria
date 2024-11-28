class Libreria:
    def __init__(self):
        # Lista che contiene tutti i libri della libreria
        self.libri = []

    def aggiungi_libro(self, titolo, autore):
        """Aggiunge un libro alla libreria."""
        libro = {
            'titolo': titolo,
            'autore': autore,
            'disponibile': True  # Se il libro è disponibile o no
        }
        self.libri.append(libro)
        print(f"Libro '{titolo}' aggiunto con successo.")

    def prestito_libro(self, titolo):
        """Presta un libro se disponibile."""
        for libro in self.libri:
            if libro['titolo'] == titolo:
                if libro['disponibile']:
                    libro['disponibile'] = False
                    print(f"Libro '{titolo}' prestato con successo.")
                    return
                else:
                    print(f"Il libro '{titolo}' non è disponibile per il prestito.")
                    return
        print(f"Il libro '{titolo}' non è stato trovato nella libreria.")

    def riporta_libro(self, titolo):
        """Riporta un libro nella libreria e lo rende disponibile."""
        for libro in self.libri:
            if libro['titolo'] == titolo:
                if not libro['disponibile']:
                    libro['disponibile'] = True
                    print(f"Libro '{titolo}' restituito con successo.")
                    return
                else:
                    print(f"Il libro '{titolo}' è già disponibile nella libreria.")
                    return
        print(f"Il libro '{titolo}' non è stato trovato nella libreria.")

    def disponibilita_libro(self, titolo):
        """Verifica la disponibilità di un libro."""
        for libro in self.libri:
            if libro['titolo'] == titolo:
                if libro['disponibile']:
                    print(f"Il libro '{titolo}' è disponibile.")
                else:
                    print(f"Il libro '{titolo}' non è disponibile.")
                return
        print(f"Il libro '{titolo}' non è stato trovato nella libreria.")

    def mostra_libri_disponibili(self):
        """Mostra tutti i libri disponibili nella libreria."""
        libri_disponibili = [libro for libro in self.libri if libro['disponibile']]
        if libri_disponibili:
            print("Libri disponibili:")
            for libro in libri_disponibili:
                print(f"- {libro['titolo']} di {libro['autore']}")
        else:
            print("Non ci sono libri disponibili al momento.")

    def mostra_libri_in_prestito(self):
        """Mostra tutti i libri attualmente in prestito."""
        libri_in_prestito = [libro for libro in self.libri if not libro['disponibile']]
        if libri_in_prestito:
            print("Libri in prestito:")
            for libro in libri_in_prestito:
                print(f"- {libro['titolo']} di {libro['autore']}")
        else:
            print("Non ci sono libri in prestito al momento.")

def menu():
    libreria = Libreria()

    while True:
        print("\n--- Menu ---")
        print("1. Aggiungi libro")
        print("2. Prestito libro")
        print("3. Riporta libro")
        print("4. Disponibilità libro")
        print("5. Libri disponibili nella libreria")
        print("6. Libri dati in prestito")
        print("7. Esci")
        
        scelta = input("Scegli un'opzione (1-7): ")

        if scelta == '1':
            titolo = input("Inserisci il titolo del libro: ")
            autore = input("Inserisci l'autore del libro: ")
            libreria.aggiungi_libro(titolo, autore)

        elif scelta == '2':
            titolo = input("Inserisci il titolo del libro da prestare: ")
            libreria.prestito_libro(titolo)

        elif scelta == '3':
            titolo = input("Inserisci il titolo del libro da riportare: ")
            libreria.riporta_libro(titolo)

        elif scelta == '4':
            titolo = input("Inserisci il titolo del libro di cui verificare la disponibilità: ")
            libreria.disponibilita_libro(titolo)

        elif scelta == '5':
            libreria.mostra_libri_disponibili()

        elif scelta == '6':
            libreria.mostra_libri_in_prestito()

        elif scelta == '7':
            print("Uscita dal programma...")
            break

        else:
            print("Opzione non valida, prova di nuovo.")

# Avvia il programma
menu()
