# Review: Cicaplast Baume B5+ La Roche-Posay

- Formato: vertical 1080x1920, 30 fps, 62 s (Shorts, Reels, TikTok)
- Narração: voz sintética (vidIQ / ElevenLabs, voz "Sarah"), arquivo `narracao.mp3`
- Visual: foto do anúncio + cards de texto (`cards/C01.png` … `C09.png`), zoom lento
- Selo "PUBLI · link de afiliado" fixo na tela o vídeo todo

| Início | Card | Narração |
|---|---|---|
| 0:00 | C01 Vale a pena? | Cicaplast Baume B5+, da La Roche-Posay. Vale a pena? |
| 0:05 | C02 Eu sou afiliado | Antes de tudo: eu sou afiliado. Se você comprar pelo meu link, eu ganho uma comissão, e você não paga nada a mais por isso. |
| 0:14 | C03 Pra quem é | É um creme multirreparador para pele sensível, ressecada ou irritada. |
| 0:19 | C04 O que tem dentro | Na fórmula tem pantenol, que é a vitamina B5, madecassosídeo, zinco, cobre, manganês e a água termal da marca. |
| 0:29 | C05 A promessa | A promessa, escrita na própria embalagem, é acelerar e melhorar a reparação da barreira da pele. |
| 0:35 | C06 Rosto e corpo | Dá pra usar no rosto e no corpo, e a marca indica para a família toda, inclusive bebês. |
| 0:41 | C07 Atenção | Um ponto de atenção: a textura é de bálsamo, mais grossinha. Se a sua pele é oleosa, usa só um pouquinho. |
| 0:49 | C08 4,9 · +100 mil vendidos | No Mercado Livre, ele tem nota 4,9 e mais de cem mil vendidos. O tubo é de 40 ml. |
| 0:57 | C09 Link na descrição | O link está na descrição. Confere o preço de hoje por lá. |

O roteiro não diz "eu usei" nem "na minha pele", porque o vídeo é montado com a foto do anúncio. Se você usar o produto de verdade, grave um take seu aplicando e troque a frase do C07 pela sua experiência.

## Refazer o vídeo

`python3 cards.py && ./render.sh` (precisa de Pillow e ffmpeg). Se trocar a narração, ajuste os tempos em `CORTES` no `render.sh`.
