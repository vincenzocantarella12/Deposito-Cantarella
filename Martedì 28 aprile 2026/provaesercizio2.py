def stampa_veicoli(self):
    for v in self.veicoli:
        print(f"Targa: {v.get_targa()} | Tipo: {v.get_tipo()} | Carico: {v._carico_attuale} kg")
        print("-" * 40)