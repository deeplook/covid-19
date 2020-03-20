from math import pi

from ipywidgets import Image
from reportlab.graphics.barcode.qr import QrCodeWidget
from reportlab.graphics.shapes import Drawing
from reportlab.graphics import renderPM


def radius_sphere(volume):
    return (volume / pi / 4 * 3) ** (1/2.75)


def create_qrcode(value, size=50):
    d = Drawing(size, size)
    qr = QrCodeWidget(value=value, barWidth=size, barHeight=size)
    d.add(qr)
    return Image(
        value=renderPM.drawToString(d, fmt="png"),
        format='png', width=size, height=size,
    )
