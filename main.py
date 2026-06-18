import math
from operator import truediv
from symtable import Class
from tokenize import String

import math
from xml.dom import ValidationErr


class InputsService:

    def input_prefix(self):
        while True:
            response = input("\n❔Which Prefix do you want? (8/16/24): ").lower().strip()
            if response == '8':
                print("\n❌not Implemented")
            if response == '16':
                print("\n❌not Implemented")
            if response == '24':
                basicnetwork, subnetwork, netzgroesse, hostanzahl, subnetzmaske = self.input_Prefix24()
                return basicnetwork, subnetwork, netzgroesse, hostanzahl, subnetzmaske
            else:
                print("\nPlease enter '8' or '16' or '24'.")

    def input_Prefix24(self):
        max24: int = 128

        while True:
            response = input("\n❔(/24) Do you want to set the IP your self?  (y/n): ").lower().strip()
            if response in ('y', 'yes'):
                basicnetwork = input("❔(/24) Please put in a Basicnetwork: ").strip()
                break
            elif response in ('n', 'no'):
                basicnetwork = "192.168.4.0"
                break
            else:
                print("🔄Please enter 'y' or 'n'")

        while True:
            try:
                subnetwork = int(input("❔How many Networks should be created: "))
                if subnetwork > max24:
                    print("\nThe max is 128.")
                    continue
                break
            except ValueError:
                print("\nPlease enter a number between 0 and 255.")

        self.calculator = Calculator()

        netzgroesse, hostanzahl, subnetzmaske = self.calculator.calculate24(subnetwork)
        return basicnetwork, subnetwork, netzgroesse, hostanzahl, subnetzmaske


class OutputsService:
    def output_console(self, hostanzahl, subnetzmaske, netzadressen):
        print(f"\n✅Max {hostanzahl} Hosts per Network possible.")
        print(f"✅New Subnetmasks: {subnetzmaske}")
        for index, adresse in enumerate(netzadressen, start=1):
            print(f"\n{index}. Network: {adresse}")
        if hostanzahl <= 0:
            print("\n⚠️ There are 0 Host possible.")



class Calculator:
    def calculate24(self, subnetwork: int):
        # 1. Nächsthöhere 2er-Potenz aus der Anzahl der benötigten Subnetze

        #new
        #subnetwork = subnetwork - 2

        #old
        bit = math.ceil(math.log2(subnetwork))

        # 2. Anzahl möglicher Hosts je Netz (Netzgröße minus Netz- und Broadcast-Adresse)
        netzgroesse = 2 ** (8 - bit)
        hostanzahl = netzgroesse -2

        # 3. Neue Subnetzmaske aus den genutzten Bits
        letztes_oktett_maske = 256 - netzgroesse
        subnetzmaske = f"255.255.255.{letztes_oktett_maske}"

        return netzgroesse, hostanzahl, subnetzmaske


class BasisnetzwerkCalculator:
    def calculate(self, subnetwork: int, basicnetwork: str, netzgroesse: list):
        netzadressen = []
        for index in range(subnetwork):
            letztes_oktett = index * netzgroesse
            teile = basicnetwork.split('.')
            teile[3] = str(int(letztes_oktett))
            netzadressen.append('.'.join(teile))

        return netzadressen


class IPCalculator:
    def __init__(self):
        self.calculator = Calculator()
        self.inputs_service = InputsService()
        self.BasicCal = BasisnetzwerkCalculator()
        self.outputs_service = OutputsService()

    def calculate_ips(self):
        while True:
            basicnetwork, subnetwork, netzgroesse, hostanzahl, subnetzmaske = self.inputs_service.input_prefix()

            netzadressen = self.BasicCal.calculate(subnetwork, basicnetwork, netzgroesse)
            # 4. Letztes Oktett jedes Netzes aus der neuen Netzgröße berechnen

            self.outputs_service.output_console(hostanzahl, subnetzmaske, netzadressen)

            response = input("\nDo you want to repeat it?  (y/n): ").lower().strip()
            if response in ('y', 'yes'):
                continue
            elif response in ('n', 'no'):
                print("\nGoodbye Version S.2.1")
                return True
            else:
                print("Please enter 'y' or 'n'.")


if __name__ == "__main__":
    IPCalculator().calculate_ips()
