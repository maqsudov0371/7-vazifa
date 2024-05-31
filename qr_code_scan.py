import segno


def qr_code_make(link, name):
    qr_code = segno.qr_code_make(link)


    qr_code.save(
        name + '.png',
        scale= 7,
        border= 13

    )
