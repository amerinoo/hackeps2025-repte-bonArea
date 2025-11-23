from opcua import Client, ua

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

    value = ua.DataValue(ua.Variant(2, ua.VariantType.Int16))
    temps_on.set_value(value)

    # Leer de vuelta para comprobar
    read_back = temps_on.get_value()
    print("ON:", read_back)

    temps_off = client.get_node('ns=3;s="DATA_HACK_NS2"."TEMPS_OFF"')

    value = ua.DataValue(ua.Variant(3, ua.VariantType.Int16))
    temps_off.set_value(value)

    # Leer de vuelta para comprobar
    read_back = temps_off.get_value()
    print("OFF:", read_back)


finally:
    client.disconnect()
    print("Desconectado")
