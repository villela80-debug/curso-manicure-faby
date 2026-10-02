"""Gera os cards 1080x1920 do review do Cicaplast Baume B5+."""
from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 1080, 1920
AZUL = (0, 133, 202)
AZUL_CLARO = (226, 241, 250)
TINTA = (20, 34, 48)
CINZA = (84, 98, 112)
FONTE_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONTE = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

CENAS = [
    ("Cicaplast Baume B5+\nvale a pena?", "La Roche-Posay · 40 ml"),
    ("Eu sou afiliado", "Comissão pra mim.\nPreço igual pra você."),
    ("Pra quem é", "Pele sensível,\nressecada ou irritada"),
    ("O que tem dentro", "Pantenol (vitamina B5)\nMadecassosídeo\nZinco · cobre · manganês\nÁgua termal da marca"),
    ("A promessa", "\"Acelera e melhora a reparação\nda barreira da pele\"\n(escrito na embalagem)"),
    ("Rosto e corpo", "A marca indica pra família toda,\ninclusive bebês"),
    ("Atenção", "Textura de bálsamo, mais grossinha.\nPele oleosa: use pouquinho."),
    ("★ 4,9 · +100 mil vendidos", "no Mercado Livre\nTubo de 40 ml"),
    ("Link na descrição", "Confere o preço de hoje"),
]


def fonte(caminho, tam):
    return ImageFont.truetype(caminho, tam)


def centralizado(d, y, texto, f, cor, espaco=14):
    for linha in texto.split("\n"):
        w = d.textlength(linha, font=f)
        d.text(((W - w) / 2, y), linha, font=f, fill=cor)
        y += f.size + espaco
    return y


def ajusta(d, texto, caminho, tam, largura_max):
    while tam > 30:
        f = fonte(caminho, tam)
        if max(d.textlength(l, font=f) for l in texto.split("\n")) <= largura_max:
            return f
        tam -= 2
    return fonte(caminho, tam)


def fundo():
    im = Image.new("RGB", (W, H), (255, 255, 255))
    d = ImageDraw.Draw(im)
    for y in range(H):
        t = y / H
        cor = tuple(int(255 * (1 - t) + c * t) for c in AZUL_CLARO)
        d.line([(0, y), (W, y)], fill=cor)
    return im


def main():
    produto = Image.open("produto.png").convert("RGB")
    lado = 900
    produto = produto.resize((lado, int(produto.height * lado / produto.width)), Image.LANCZOS)
    mascara = Image.new("L", produto.size, 0)
    ImageDraw.Draw(mascara).rounded_rectangle([0, 0, *produto.size], radius=48, fill=255)
    sombra = Image.new("RGBA", (produto.width + 80, produto.height + 80), (0, 0, 0, 0))
    ImageDraw.Draw(sombra).rounded_rectangle(
        [40, 52, produto.width + 40, produto.height + 52], radius=48, fill=(0, 60, 100, 60))
    sombra = sombra.filter(ImageFilter.GaussianBlur(22))

    for i, (titulo, sub) in enumerate(CENAS, 1):
        im = fundo()
        d = ImageDraw.Draw(im)

        # selo de publicidade, fixo em todas as cenas
        selo = "PUBLI · link de afiliado"
        fs = fonte(FONTE_B, 34)
        sw = d.textlength(selo, font=fs)
        d.rounded_rectangle([(W - sw) / 2 - 28, 70, (W + sw) / 2 + 28, 132], radius=31, fill=AZUL)
        d.text(((W - sw) / 2, 82), selo, font=fs, fill="white")

        x, y = (W - produto.width) // 2, 180
        im.paste(sombra, (x - 40, y - 40), sombra)
        im.paste(produto, (x, y), mascara)

        topo = y + produto.height + 70
        ft = ajusta(d, titulo, FONTE_B, 84, W - 120)
        yy = centralizado(d, topo, titulo, ft, TINTA, 18)
        d.rounded_rectangle([W / 2 - 60, yy + 18, W / 2 + 60, yy + 28], radius=5, fill=AZUL)
        fsub = ajusta(d, sub, FONTE, 50, W - 120)
        centralizado(d, yy + 70, sub, fsub, CINZA, 16)

        im.save(f"cards/C{i:02d}.png")


if __name__ == "__main__":
    main()
