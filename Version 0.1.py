import math


class InputsService:
    def input_console(self):
        basicnetwork = input("Bitte geben sie das Basisnetz ein (/24): ").strip()
        subnetwork = int(input("Wieviele Netze sollen erstellt werden: "))
        return basicnetwork, subnetwork


class Calculator:
    def calculate(self, subnetwork: int):
        # 1. Nächsthöhere 2er-Potenz aus der Anzahl der benötigten Subnetze
        bit = math.ceil(math.log2(subnetwork))

        # 2. Anzahl möglicher Hosts je Netz (Netzgröße minus Netz- und Broadcast-Adresse)
        netzgroesse = 2 ** (8 - bit)
        hostanzahl = netzgroesse - 2

        # 3. Neue Subnetzmaske aus den genutzten Bits
        letztes_oktett_maske = 256 - netzgroesse
        subnetzmaske = f"255.255.255.{letztes_oktett_maske}"

        return netzgroesse, hostanzahl, subnetzmaske


class OutputsService:
    def output_console(self, hostanzahl, subnetzmaske, netzadressen):
        print(f"Maximal {hostanzahl} Hosts sind pro Netz adressierbar.")
        print(f"Neue Subnetzmaske: {subnetzmaske}")
        for index, adresse in enumerate(netzadressen, start=1):
            print(f"{index}. Netz: {adresse}")


class IPCalculator:
    def __init__(self):
        self.calculator = Calculator()
        self.inputs_service = InputsService()
        self.outputs_service = OutputsService()

    def calculate_ips(self):
        while True:
            basicnetwork, subnetwork = self.inputs_service.input_console()
            netzgroesse, hostanzahl, subnetzmaske = self.calculator.calculate(subnetwork)

            # 4. Letztes Oktett jedes Netzes aus der neuen Netzgröße berechnen
            netzadressen = []
            for index in range(subnetwork):
                letztes_oktett = index * netzgroesse
                teile = basicnetwork.split('.')
                teile[3] = str(int(letztes_oktett))
                netzadressen.append('.'.join(teile))

            self.outputs_service.output_console(hostanzahl, subnetzmaske, netzadressen)

            response = input("\nDo you want to repeat it?  (y/n): ").lower().strip()
            if response in ('y', 'yes'):
                continue
            elif response in ('n', 'no'):
                print("\nGoodbye Version S.1.4")
                return True
            else:
                print("Please enter 'y' or 'n'.")


if __name__ == "__main__":
    IPCalculator().calculate_ips()