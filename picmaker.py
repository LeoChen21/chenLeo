def main():
    body = ''

    
    for i in range(500):
        for j in range(500):
            r = i % 255
            g = j % 255
            b = (i + j) % 255

            body += str(r) + ' ' + str(g) + ' ' + str(b) + ' '
        body += '\n'

    #ppm
    pic = open('image.ppm', 'w')
    pic.write('P3\n500 500\n255\n')
    pic.write(body)
    pic.close()

main()
