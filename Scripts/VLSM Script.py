def htbit(host_num):
    y = 0
    z = 0
    while host_num > z:
        x = pow(2, y)
        y += 1
        z = x - 2
    return y - 1


'''def ippulsold(ip, ipf):
    ipr = [0, 0, 0, 0]
    for i in range(3, -1, -1):
        if (ip[i] + ipf[i]) < 255:
            ipr[i] = ip[i] + ipf[i]
        elif (ip[i] + ipf[i]) > 255:
            ipf[(i - 1)] += 1
            ipr[i] = ((ip[i] + ipf[i]) - 255)
    return ipr'''

def ippuls(ip, ipf):
    ipr = [0, 0, 0, 0]
    for i in range(3, -1, -1):
        if (ip[i] + ipf[i]) <= 255:
            ipr[i] = ip[i] + ipf[i]
        elif (ip[i] + ipf[i]) > 255:
            ipf[(i - 1)] = (ip[i] + ipf[i]) - 255
            ipr[i] = 0
    return ipr

def broadast(network_ad, host_bit):
    y = pow(2, host_bit) - 1
    x = [0, 0, 0, 0]
    # Cal Value Of X
    for i in range(3, -1, -1):
        if y <= 255:
            x = [0, 0, 0, y]
        elif y <= 65535:
            x = [0, 0, int((y - 255) / 255), 255]
        elif y <= 16777215:
            x = [0, int((y - 65535) / 65535), 255, 255]
        elif y <= (pow(2, 32) - 1):
            x = [int((y - 16777215) / 16777215), 255, 255, 255]
        else:
            print("Error on brodcast Funsation or Invalid Input")


    # Vlaue Of X Adding with Network_ad

    ops = [0, 0, 0, 0]
    for i in range(3, -1, -1):
        ipr = [0, 0, 0, 0]
        if (x[i] + network_ad[i]) <= 255:
            ipr[i] = network_ad[i] + x[i]
            ops[i] = ipr[i]
        elif (x[i] + network_ad[i]) > 255:
            ipr[i] = 255
            ipr[(i - 1)] += (x[i] + network_ad[i]) - 255
            ops[i] = ipr[i]
            ops[(i - 1)] = ipr[(i - 1)]
    return ops


def subnetmask(hostb):
    y = 32 - hostb
    x = [0, 0, 0, 0]

    for i in range(4):

        if y >= 8:
            y -= 8
            x[i] = 255

        elif y < 8 and y > 0:
            tem = 0

            for j in range((8 - y), 8):
                z = pow(2, j)
                tem += z
                x[i] = tem
                y -= y
    return x


# Start From Hare --------------------------------------------------------------------------------------------------

def startscript():
    print(
        "\n  Welcome To IP Address VLSM Calculation Script \n"
        "\n       Created By Abdur Rashid Mondal  "
        "\n          Student Of MSME (CTTC) "
        "\n=============================================================")

    # doted IP convert into List data
    fristIP = [10, 0, 0, 0]

    e, f, g, h = input("Enter Strating Address ex(192.168.0.0) : ").split(".")
    a = int(e)
    b = int(f)
    c = int(g)
    d = int(h)

    oip = [a, b, c, d]

    if (len(oip)) == 4:
        fristIP = oip
    elif (len(oip)) < 4:
        print("Error Missing Octet \n Please Enter 4 Octet IPv4 Address ")
    elif (len(oip)) > 4:
        print("Error Too many Octet \n Please Enter 4 Octet IPv4 Address ")

    department = int(input("How Many Department : "))
    print('''
                    ******** Remember *******
    All Department Should be sorted Descending order with Host Numbers
    -------------------------------------------------------------------''')
    holdip = [0, 0, 0, 0]
    for d in range(department):
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>[Department No = {0}]<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<".format(d + 1))

        if d == 0:
            host = int(input("How Many Host In Department No {0}  : ".format(d + 1)))
            hostbit = htbit(host)
            nw = list(fristIP)
            ba = broadast(nw, hostbit)
            fva = ippuls(nw, [0, 0, 0, 1])
            lva = ippuls(ba, [0, 0, 0, -1])
            sm = subnetmask(hostbit)
            holdip = ippuls(ba,[0,0,0,1])

            # All Data Printing
            print('.....................................................')
            print("       We Reserve {0} No of Host Bit ".format(hostbit))
            print("Maximum {0} No of Host Can be Add in this Department".format((pow(2, hostbit) - 2)))
            print(".....................................................\n")
            print("Network Address   :", nw[0], ".", nw[1], ".", nw[2], ".", nw[3])
            print("Broadcast Address :", ba[0], ".", ba[1], ".", ba[2], ".", ba[3])
            print("First Valid Add   :", fva[0], ".", fva[1], ".", fva[2], ".", fva[3])
            print("Last Valid Add    :", lva[0], '.', lva[1], '.', lva[2], '.', lva[3])
            print("Subnet Mask is    :", sm[0], '.', sm[1], '.', sm[2], '.', sm[3])
        else:
            host = int(input("How Many Host In Department No {0} : ".format(d + 1)))
            hostbit = htbit(host)
            nw = holdip
            ba = broadast(nw, hostbit)
            fva = ippuls(nw, [0, 0, 0, 1])
            lva = ippuls(ba, [0, 0, 0, -1])
            sm = subnetmask(hostbit)

            print('.....................................................')
            print("       We Reserve {0} No of Host Bit ".format(hostbit))
            print("Maximum {0} No of Host Can be Add in this Department".format((pow(2, hostbit) - 2)))
            print(".....................................................\n")
            print("Network Address   :", nw[0], ".", nw[1], ".", nw[2], ".", nw[3])
            print("Broadcast Address :", ba[0], ".", ba[1], ".", ba[2], ".", ba[3])
            print("First Valid Add   :", fva[0], ".", fva[1], ".", fva[2], ".", fva[3])
            print("Last Valid Add    :", lva[0], '.', lva[1], '.', lva[2], '.', lva[3])
            print("Subnet Mask is    :", sm[0], '.', sm[1], '.', sm[2], '.', sm[3])
            holdip = ippuls(ba, [0, 0, 0, 1])
    else:
        print('''
====-===================================================================================================================
========================================================================================================================
                                        Thank You For Using This Script 
                                 ------------------------------------------------
                                 Contract :-
                                          Name  = Abdur Rashid Mondal
                                          Phone = 8159030930
                                          Email = ar.rashid.xbox@gmail.com / ar.rashid.mondal@gmail.com

========================================================================================================================
========================================================================================================================''')
        again = input("Do You want to Exit ? [y/n] :")
        if again == "y" or again == "Y" or again == "yes" or again == "Yes" or again == "YES":
            again = again
        else:
            startscript()


startscript()
