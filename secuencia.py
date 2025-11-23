from time import sleep

from opcua import Client, ua


def ns1(NS1_TEMPS_ON, NS1_TEMPS_OFF):
    import snap7
    from snap7.util import get_bool, get_sint, set_sint, set_bool

    client = snap7.client.Client()

    # Conectar al PLC S7-1500 (rack 0, slot 1)
    client.connect("10.72.101.72", 0, 1)

    # Leemos DB1, desde offset 0, 256 bytes
    data = client.db_read(1, 0, 255)
    print("RAW DATA:", data)

    set_bool(data, 0, 0, True)
    set_sint(data, 3, NS1_TEMPS_ON)  # ON
    set_sint(data, 5, NS1_TEMPS_OFF)  # OFF

    # print("User/Password:", get_string(data, 6))
    print("LED:", get_bool(data, 0, 0))
    print("ON:", get_sint(data, 3))
    print("OFF:", get_sint(data, 5))

    client.db_write(1, 0, data)
    client.disconnect()


def ns2(NS2_TEMPS_ON, NS2_TEMPS_OFF):
    # URL del servidor OPC UA del PLC
    URL = "opc.tcp://10.72.101.72:4840"

    client = Client(URL)

    try:
        client.connect()
        print("Conectado a", URL)

        led = client.get_node('ns=3;s="DATA_HACK_NS2"."ON_OFF"')

        # Escribimos un booleano True
        value = ua.DataValue(ua.Variant(True, ua.VariantType.Boolean))
        led.set_value(value)

        # Leer de vuelta para comprobar
        read_back = led.get_value()
        print("LED:", read_back)

        temps_on = client.get_node('ns=3;s="DATA_HACK_NS2"."TEMPS_ON"')

        value = ua.DataValue(ua.Variant(NS2_TEMPS_ON, ua.VariantType.Int16))
        temps_on.set_value(value)

        # Leer de vuelta para comprobar
        read_back = temps_on.get_value()
        print("ON:", read_back)

        temps_off = client.get_node('ns=3;s="DATA_HACK_NS2"."TEMPS_OFF"')

        value = ua.DataValue(ua.Variant(NS2_TEMPS_OFF, ua.VariantType.Int16))
        temps_off.set_value(value)

        # Leer de vuelta para comprobar
        read_back = temps_off.get_value()
        print("OFF:", read_back)


    finally:
        client.disconnect()
        print("Desconectado")


def main():
    for NS1_TEMPS_ON in range(11):
        for NS1_TEMPS_OFF in range(11):
            for NS2_TEMPS_ON in range(11):
                for NS2_TEMPS_OFF in range(11):
                        ns1(NS1_TEMPS_ON, NS1_TEMPS_OFF)
                        ns2(NS2_TEMPS_ON, NS2_TEMPS_OFF)
                        sleep(0.2)


if __name__ == '__main__':
    main()

    # Solution
    ns1(10, 3)
    ns2(10, 3)
