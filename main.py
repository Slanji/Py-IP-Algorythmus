import math
from operator import truediv

basenetwork = 0
subnetwork = 0
hostanzahl = 0
hostnumbers = 0
basicnetwork = 0


class Inputs:

    def IP_Calculator(basicnetwork):
        while True:
            subnetwork = int(input("\nHow many Subnetworks do you want? "))
            hostnumbers = int(input("\nHow many Hosts do you want? "))
            bit = math.ceil(math.log2(hostnumbers))
            hostanzahl = 2 ** bit
            netze = 256 / subnetwork
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
                    IP_Calculator(basicnetwork)
                    break
                else:
                    print("Please enter 'y' or 'n'.")
            break
        elif response in ('n', 'no'):
            basicnetwork = "192.168."
            while True:
                responseflase = input("\nDo you want multiply Networks?  (y/n): ").lower().strip()
                if responseflase in ('y', 'yes'):
                    print("\nFunction not implemented")
                elif responseflase in ('n', 'no'):
                    basicnetwork = basicnetwork + "4.0"
                    IP_Calculator(basicnetwork)
                    break
                else:
                    print("Please enter 'y' or 'n'.")
            break
        else:
            print("Please enter 'y' or 'n'.")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
