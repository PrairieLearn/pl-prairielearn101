def write_bar(pinList, k):
    for p in pinList[:k]:
        GPIO.output(p, GPIO.HIGH)

