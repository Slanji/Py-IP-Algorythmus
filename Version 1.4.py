import math
from operator import truediv
from symtable import Class
from tokenize import String

class InputsService:
    def input_console(self):
        subnetwork = int(input("\nHow many Subnetworks do you want? "))
        hostnumbers = int(input("\nHow many Hosts do you want? "))
        return subnetwork, hostnumbers

class OutputsService:
    def output_console(self):

class Calculator:
    def calculate(self, subnetwork: int, hostnumbers: int):
        bit = math.ceil(math.log2(hostnumbers))
        hostanzahl = 2 ** bit
        netze = 256 / subnetwork
        return hostanzahl, netze

class IPCalculator:
    def __init__(self):
        self.calculator = Calculator()
        self.inputs_service = InputsService()

    def calculate_ips(self, basicnetwork):
        subnetwork, hostnumbers = self.inputs_service.input_console()
        hostanzahl, netze = self.calculator.calculate(subnetwork, hostnumbers)

        while True:

            total = 0

            for count in range(subnetwork):
                total += hostanzahl
                parts = basicnetwork.split('.')
                parts[3] = f'{total}'
                new_ip = '.'.join(parts)

                if total > 256:
                    print(f"Error: Maximum IP's reached")
                    break
                elif hostanzahl > netze:
                    print("Error: To many subnetworks and not enough IPs")
                    break
                else:
                    print(f"Given IPs: {new_ip}")

            response = input("\nDo you want to repeat it?  (y/n): ").lower().strip()
            if response in ('y', 'yes'):
                continue
            elif response in ('n', 'no'):
                print("\nGoodbye Version S.1.4")
                return True
            else:
                print("Please enter 'y' or 'n'.")

    def Edit_prefix(basicnetwork):
        #while True:
            howmanynetworks = int(input("\nHow many networks do you want? "))
            total = 0
            for count in range(howmanynetworks):
                network = 2 ** howmanynetworks
                total += howmanynetworks
            print(howmanynetworks)

            #bit = math.ceil(math.log2())
            #hostanzahl = 2 **

class Anwendung:
    label_YesOrNo = "Please enter 'y' or 'n'."
    calculator = IPCalculator()

    while True:
        response = input("\nDo you want to set the IP your self?  (y/n): ").lower().strip()
        if response in ('y', 'yes'):
            basicnetwork = input("\nHow do you wanna call the IP? (Exempal: 192.168.4) ")
            while True:
                responseflase = input("\nDo you want multiply Networks?  (y/n): ").lower().strip()
                if responseflase in ('y', 'yes'):

                    print("\nFunction not implemented")
                elif responseflase in ('n', 'no'):
                    basicnetwork = basicnetwork + ".0"
                    IPCalculator.calculate_ips(basicnetwork)
                    break
                else:
                    print(label_YesOrNo)
            break
        elif response in ('n', 'no'):
            basicnetwork = "192.168."
            while True:
                responseflase = input("\nDo you want multiply Networks?  (y/n): ").lower().strip()
                if responseflase in ('y', 'yes'):
                    print("\nFunction not implemented")
                elif responseflase in ('n', 'no'):
                    basicnetwork = basicnetwork + "4.0"
                    calculator.calculate_ips(basicnetwork)
                    break
                else:
                    print(label_YesOrNo)
            break
        else:
            print(label_YesOrNo)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
