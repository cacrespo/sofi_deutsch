import os
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import (
    Image,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_PDF = str(REPO_ROOT / "app/static/Repaso_Aleman_Sofia_3er_Grado.pdf")
ASSETS_DIR = str(REPO_ROOT / "app/static/dandy_assets")
VOCAB_DIR = str(REPO_ROOT / "app/static/vocab_images")

PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN_X = 26
MARGIN_Y = 22
CONTENT_WIDTH = PAGE_WIDTH - (2 * MARGIN_X)

styles = getSampleStyleSheet()

# Colors
C_PRIMARY = colors.HexColor("#1e3a8a")  # Deep Navy
C_ACCENT = colors.HexColor("#b45309")  # Amber
C_GREEN = colors.HexColor("#15803d")  # Forest Green
C_BLUE = colors.HexColor("#2563eb")  # Royal Blue
C_TEXT = colors.HexColor("#1e293b")  # Slate 800
C_SUBTEXT = colors.HexColor("#64748b")  # Slate 500
C_BOX_BG = colors.HexColor("#f8fafc")  # Soft light gray
C_BOX_BORDER = colors.HexColor("#cbd5e1")  # Slate 300
C_HORTEXT_BG = colors.HexColor("#eff6ff")  # Light blue
C_HORTEXT_BORDER = colors.HexColor("#93c5fd")

# Styles matching sample exam
s_top_header = ParagraphStyle(
    "TopH", fontName="Helvetica-Bold", fontSize=12.5, leading=14.5, textColor=C_PRIMARY, alignment=1
)
s_top_sub = ParagraphStyle(
    "TopSub", fontName="Helvetica", fontSize=8.5, leading=11, textColor=C_TEXT, alignment=1
)
s_header_meta = ParagraphStyle(
    "HMeta", fontName="Helvetica", fontSize=8, leading=10, textColor=C_TEXT
)

s_sec_num = ParagraphStyle(
    "SecNum", fontName="Helvetica-Bold", fontSize=9.5, leading=12, textColor=C_PRIMARY
)
s_consigna_de = ParagraphStyle(
    "ConsDe", fontName="Helvetica-Bold", fontSize=8, leading=10, textColor=C_TEXT
)
s_consigna_es = ParagraphStyle(
    "ConsEs", fontName="Helvetica", fontSize=7.6, leading=9.5, textColor=C_SUBTEXT
)

s_box_title = ParagraphStyle(
    "BoxTitle", fontName="Helvetica-Bold", fontSize=9, leading=11, textColor=C_PRIMARY, alignment=1
)
s_box_de = ParagraphStyle(
    "BoxDe", fontName="Helvetica-Bold", fontSize=8, leading=10, textColor=C_TEXT, alignment=1
)
s_box_es = ParagraphStyle(
    "BoxEs",
    fontName="Helvetica-Oblique",
    fontSize=7.5,
    leading=9.5,
    textColor=C_SUBTEXT,
    alignment=1,
)

s_q_de = ParagraphStyle("QDe", fontName="Helvetica-Bold", fontSize=8, leading=10, textColor=C_TEXT)
s_q_es = ParagraphStyle(
    "QEs", fontName="Helvetica-Oblique", fontSize=7.4, leading=9, textColor=C_SUBTEXT
)
s_options = ParagraphStyle("Opt", fontName="Helvetica", fontSize=7.8, leading=9.5, textColor=C_TEXT)
s_normal = ParagraphStyle("Norm", fontName="Helvetica", fontSize=8, leading=10, textColor=C_TEXT)

s_badge_de = ParagraphStyle(
    "BDe", fontName="Helvetica-Bold", fontSize=7, leading=8.5, textColor=C_TEXT, alignment=1
)
s_badge_es = ParagraphStyle(
    "BEs", fontName="Helvetica-Oblique", fontSize=6.2, leading=7.5, textColor=C_SUBTEXT, alignment=1
)

s_footer_note = ParagraphStyle(
    "FootNote", fontName="Helvetica-Oblique", fontSize=7, leading=8.5, textColor=C_SUBTEXT
)
s_points = ParagraphStyle(
    "Pts", fontName="Helvetica-Bold", fontSize=8, leading=10, textColor=C_PRIMARY, alignment=2
)


def create_page_top(title_text, subtitle_text, toon_name, toon_file, page_num):
    img_path = os.path.join(ASSETS_DIR, toon_file)
    img = (
        Image(img_path, width=32, height=32)
        if os.path.exists(img_path)
        else Paragraph("⭐", s_sec_num)
    )

    t_data = [
        [
            img,
            [
                Paragraph("<b>DEUTSCH – 3.º GRADO</b>", s_top_header),
                Paragraph(f"<b>Material de práctica · {title_text}</b>", s_top_sub),
                Paragraph(
                    f"<font size='7' color='#64748b'>Dandy's World mit <b>{toon_name}</b> • Frau Mónica Briesemeister • Prüfung: 19. November</font>",
                    s_header_meta,
                ),
            ],
            Paragraph(
                f"<para align='right'><font size='7.5'><b>Seite {page_num} / 5</b></font><br/><font size='6.5' color='#64748b'>deutsch.hurlingham.xyz</font></para>",
                s_header_meta,
            ),
        ]
    ]
    t = Table(t_data, colWidths=[36, CONTENT_WIDTH - 110, 74])
    t.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )
    return t


def create_name_date_bar():
    t_data = [
        [
            Paragraph("<b>Nombre / Name:</b> ____________________________________", s_header_meta),
            Paragraph(
                "<para align='right'><b>Fecha / Datum:</b> Donnerstag, 19. November</para>",
                s_header_meta,
            ),
        ]
    ]
    t = Table(t_data, colWidths=[CONTENT_WIDTH * 0.6, CONTENT_WIDTH * 0.4])
    t.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
                ("TOPPADDING", (0, 0), (-1, -1), 1),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )
    return t


def create_consigna_block(number_str, title_de_es, aufgabe_de, consigna_es):
    content = [
        [Paragraph(f"<b>{number_str}. {title_de_es}</b>", s_sec_num)],
        [Paragraph(f"<b>Aufgabe / Consigna:</b> {aufgabe_de}", s_consigna_de)],
        [Paragraph(consigna_es, s_consigna_es)],
    ]
    t = Table(content, colWidths=[CONTENT_WIDTH])
    t.setStyle(
        TableStyle(
            [
                ("TOPPADDING", (0, 0), (-1, -1), 1),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )
    return t


def create_text_card(
    title, lines_de, lines_es, bg_color=C_HORTEXT_BG, border_color=C_HORTEXT_BORDER
):
    content = []
    if title:
        content.append([Paragraph(f"<b>{title}</b>", s_box_title)])
    for line in lines_de:
        content.append([Paragraph(line, s_box_de)])
    if lines_es:
        content.append([Spacer(1, 1)])
        for line in lines_es:
            content.append([Paragraph(line, s_box_es)])

    t = Table(content, colWidths=[CONTENT_WIDTH])
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), bg_color),
                ("BOX", (0, 0), (-1, -1), 1, border_color),
                ("ROUNDEDCORNERS", [6, 6, 6, 6]),
                ("TOPPADDING", (0, 0), (-1, -1), 2),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
            ]
        )
    )
    return t


def create_question_item(q_num, q_de, q_es, opt_a, opt_b, opt_c):
    content = [
        [
            Paragraph(f"<b>{q_num}. {q_de}</b>", s_q_de),
        ],
        [
            Paragraph(q_es, s_q_es),
        ],
        [
            Paragraph(
                f"[  ] a) {opt_a} &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [  ] b) {opt_b} &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [  ] c) {opt_c}",
                s_options,
            )
        ],
    ]
    t = Table(content, colWidths=[CONTENT_WIDTH])
    t.setStyle(
        TableStyle(
            [
                ("TOPPADDING", (0, 0), (-1, -1), 1),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
                ("LEFTPADDING", (0, 0), (-1, -1), 3),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )
    return t


def create_visual_vocab_strip(items, cols=6):
    """
    items: list of (icon_filename, german_label, spanish_label, border_color_hex)
    """
    rows = []
    cur_row = []
    for icon_fn, de_lbl, es_lbl, b_col in items:
        icon_p = os.path.join(VOCAB_DIR, icon_fn)
        img = (
            Image(icon_p, width=22, height=22)
            if os.path.exists(icon_p)
            else Paragraph("📌", s_badge_de)
        )
        cell = [img, Paragraph(f"<b>{de_lbl}</b>", s_badge_de), Paragraph(es_lbl, s_badge_es)]
        cell_t = Table([[c] for c in cell], colWidths=[CONTENT_WIDTH / cols - 6])
        cell_t.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#f8fafc")),
                    ("BOX", (0, 0), (-1, -1), 0.8, colors.HexColor(b_col)),
                    ("ROUNDEDCORNERS", [4, 4, 4, 4]),
                    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                    ("TOPPADDING", (0, 0), (-1, -1), 1),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
                    ("LEFTPADDING", (0, 0), (-1, -1), 1),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 1),
                ]
            )
        )
        cur_row.append(cell_t)
        if len(cur_row) == cols:
            rows.append(cur_row)
            cur_row = []
    if cur_row:
        while len(cur_row) < cols:
            cur_row.append("")
        rows.append(cur_row)

    t = Table(rows, colWidths=[CONTENT_WIDTH / cols] * cols)
    t.setStyle(
        TableStyle(
            [
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("TOPPADDING", (0, 0), (-1, -1), 1),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
                ("LEFTPADDING", (0, 0), (-1, -1), 1),
                ("RIGHTPADDING", (0, 0), (-1, -1), 1),
            ]
        )
    )
    return t


def build_pdf():
    doc = SimpleDocTemplate(
        OUTPUT_PDF,
        pagesize=A4,
        leftMargin=MARGIN_X,
        rightMargin=MARGIN_X,
        topMargin=MARGIN_Y,
        bottomMargin=MARGIN_Y,
    )

    story = []

    # =========================================================================
    # PAGE 1: Hörverstehen – Max stellt sich vor & Personalvorstellung
    # =========================================================================
    story.append(
        create_page_top(
            "Presentación personal y de otra persona",
            "DEUTSCH 3° GRADO",
            "Max & Dandy",
            "dandy.png",
            1,
        )
    )
    story.append(Spacer(1, 2))
    story.append(create_name_date_bar())
    story.append(Spacer(1, 3))

    story.append(
        create_consigna_block(
            "1",
            "Hörverstehen – Escuchá y marcá",
            "Hör gut zu und kreuze die richtige Antwort an.",
            "Escuchá atentamente y marcá con una X la respuesta correcta.",
        )
    )
    story.append(Spacer(1, 3))

    lines_de_p1 = [
        "Hallo! Ich heiße Max. Ich bin 8 Jahre alt.",
        "Ich habe einen Hund. Der Hund heißt Bello.",
        "Ich spiele gern Fußball. Meine Lieblingsfarbe ist blau.",
    ]
    lines_es_p1 = [
        "¡Hola! Me llamo Max. Tengo 8 años. Tengo un perro. El perro se llama Bello.",
        "Me gusta jugar al fútbol. Mi color favorito es el azul.",
    ]
    story.append(
        create_text_card("Hörtext – Max stellt sich vor (Dandy's World)", lines_de_p1, lines_es_p1)
    )
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>Fragen / Preguntas:</b>", s_sec_num))
    story.append(Spacer(1, 1))

    story.append(
        create_question_item(
            "1", "Wie heißt der Junge?", "¿Cómo se llama el nene?", "Leo", "Max", "Bello"
        )
    )
    story.append(Spacer(1, 1.5))
    story.append(
        create_question_item(
            "2", "Wie alt ist er?", "¿Cuántos años tiene?", "7 Jahre", "8 Jahre", "9 Jahre"
        )
    )
    story.append(Spacer(1, 1.5))
    story.append(
        create_question_item(
            "3",
            "Welches Tier hat er?",
            "¿Qué animal tiene?",
            "Eine Katze",
            "Ein Pferd",
            "Einen Hund (Bello)",
        )
    )
    story.append(Spacer(1, 1.5))
    story.append(
        create_question_item(
            "4", "Was spielt er gern?", "¿Qué le gusta jugar?", "Fußball", "Schwimmen", "Malen"
        )
    )
    story.append(Spacer(1, 1.5))
    story.append(
        create_question_item(
            "5",
            "Was ist seine Lieblingsfarbe?",
            "¿Cuál es su color favorito?",
            "Rot",
            "Grün",
            "Blau",
        )
    )
    story.append(Spacer(1, 2))

    bot_table_p1 = [
        [Paragraph("<b>Punkte / Puntaje: ______ / 10</b>", s_points)],
        [
            Paragraph(
                "<i>Para practicar en casa:</i> una persona adulta o la web interactiva (<b>deutsch.hurlingham.xyz</b>) puede leer el texto en alemán en voz alta con el botón 🎧. La traducción al español sirve como ayuda.",
                s_footer_note,
            )
        ],
    ]
    t_bot_p1 = Table(bot_table_p1, colWidths=[CONTENT_WIDTH])
    t_bot_p1.setStyle(
        TableStyle(
            [
                ("TOPPADDING", (0, 0), (-1, -1), 1),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )
    story.append(t_bot_p1)

    story.append(PageBreak())

    # =========================================================================
    # PAGE 2: Leseverstehen – Das ist Anna! & Jetzt bist du dran!
    # =========================================================================
    story.append(
        create_page_top(
            "Presentación de otra persona & Producción personal",
            "DEUTSCH 3° GRADO",
            "Anna & Poppy",
            "poppy.png",
            2,
        )
    )
    story.append(Spacer(1, 2))

    story.append(
        create_consigna_block(
            "2",
            "Leseverstehen – Leé y comprendé",
            "Lies den Text und kreuze die richtige Antwort an.",
            "Leé el texto y marcá con una X la respuesta correcta.",
        )
    )
    story.append(Spacer(1, 2))

    lines_de_p2 = [
        "Hallo! Das ist meine Freundin Anna. Sie ist 9 Jahre alt und kommt aus Deutschland.",
        "Sie hat eine Katze. Die Katze heißt Mimi. Anna spielt gern Tennis und malt gern. Ihre Lieblingsfarbe ist rosa.",
    ]
    lines_es_p2 = [
        "¡Hola! Esta es mi amiga Anna. Tiene 9 años y es de Alemania. Tiene una gata (Mimi).",
        "A Anna le gusta jugar al tenis y pintar. Su color favorito es el rosa.",
    ]
    story.append(
        create_text_card(
            "Lesetext – Das ist Anna!",
            lines_de_p2,
            lines_es_p2,
            colors.HexColor("#fdf4ff"),
            colors.HexColor("#e879f9"),
        )
    )
    story.append(Spacer(1, 2))

    story.append(Paragraph("<b>Fragen / Preguntas:</b>", s_sec_num))
    story.append(Spacer(1, 1))

    story.append(
        create_question_item(
            "1", "Wie heißt das Mädchen?", "¿Cómo se llama la nena?", "Lisa", "Anna", "Mimi"
        )
    )
    story.append(Spacer(1, 1))
    story.append(
        create_question_item(
            "2", "Wie alt ist Anna?", "¿Cuántos años tiene Anna?", "8 Jahre", "9 Jahre", "10 Jahre"
        )
    )
    story.append(Spacer(1, 1))
    story.append(
        create_question_item(
            "3",
            "Welches Tier hat Anna?",
            "¿Qué animal tiene Anna?",
            "Einen Hund",
            "Ein Pferd",
            "Eine Katze (Mimi)",
        )
    )
    story.append(Spacer(1, 1))
    story.append(
        create_question_item(
            "4",
            "Was macht Anna gern?",
            "¿Qué le gusta hacer a Anna?",
            "Tennis spielen und malen",
            "Fußball spielen",
            "Schwimmen",
        )
    )
    story.append(Spacer(1, 1))
    story.append(
        create_question_item(
            "5",
            "Was ist ihre Lieblingsfarbe?",
            "¿Cuál es su color favorito?",
            "Blau",
            "Rosa",
            "Grün",
        )
    )
    story.append(Spacer(1, 2))
    story.append(Paragraph("<b>Punkte / Puntaje: ______ / 10</b>", s_points))
    story.append(Spacer(1, 2))

    story.append(
        create_consigna_block(
            "3",
            "Jetzt bist du dran! – ¡Ahora te toca a vos!",
            "Ergänze die Sätze mit deinen persönlichen Informationen.",
            "Completá las oraciones con tus datos personales.",
        )
    )
    story.append(Spacer(1, 1.5))

    p3_form = [
        [
            Paragraph(
                "Hallo! Ich heiße ____________________________________________________________________.",
                s_normal,
            )
        ],
        [
            Paragraph(
                "Ich bin _________ Jahre alt. Ich wohne in ______________________________________________.",
                s_normal,
            )
        ],
        [
            Paragraph(
                "Ich habe _________________________________ (ein Haustier / ein Spielzeug).",
                s_normal,
            )
        ],
        [
            Paragraph(
                "Mein Lieblingstier ist _______________________________________________________________.",
                s_normal,
            )
        ],
        [
            Paragraph(
                "Ich spiele gern ______________________________________________________________________.",
                s_normal,
            )
        ],
        [
            Paragraph(
                "Meine Lieblingsfarbe ist _____________________________________________________________.",
                s_normal,
            )
        ],
        [
            Paragraph(
                "<b>Extra:</b> Zeichne dich selbst und male dein Lieblingstier! <i>(Dibujate y coloreá tu animal favorito)</i>",
                s_header_meta,
            )
        ],
    ]
    t_p3 = Table(p3_form, colWidths=[CONTENT_WIDTH])
    t_p3.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#fffbeb")),
                ("BOX", (0, 0), (-1, -1), 1, colors.HexColor("#fde68a")),
                ("ROUNDEDCORNERS", [6, 6, 6, 6]),
                ("TOPPADDING", (0, 0), (-1, -1), 1.5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 1.5),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
            ]
        )
    )
    story.append(t_p3)

    story.append(PageBreak())

    # =========================================================================
    # PAGE 3: Schulsachen & Artikel (Der, Die, Das) MIT BILDERN
    # =========================================================================
    story.append(
        create_page_top(
            "Útiles escolares y artículos (der / die / das)",
            "DEUTSCH 3° GRADO",
            "Boxten",
            "boxten.png",
            3,
        )
    )
    story.append(Spacer(1, 2))

    story.append(
        create_consigna_block(
            "4",
            "Schulsachen & Artikel – Útiles escolares y artículos con imágenes",
            "Schau dir die Bilder an und wähle den richtigen Artikel aus (der, die, das / ein, eine, kein).",
            "Mirá las imágenes de los útiles y marcá con una X el artículo correcto.",
        )
    )
    story.append(Spacer(1, 2))

    # Strip visual de útiles escolares
    school_visuals = [
        ("bleistift_icon.png", "der Bleistift", "el lápiz", "#1d4ed8"),
        ("radiergummi_icon.png", "der Radiergummi", "la goma", "#1d4ed8"),
        ("schere_icon.png", "die Schere", "la tijera", "#b91c1c"),
        ("schultasche_icon.png", "die Schultasche", "la mochila", "#b91c1c"),
        ("maeppchen_icon.png", "das Mäppchen", "la cartuchera", "#15803d"),
        ("lineal_icon.png", "das Lineal", "la regla", "#15803d"),
        ("buch_icon.png", "das Buch", "el libro", "#15803d"),
        ("heft_icon.png", "das Heft", "el cuaderno", "#15803d"),
        ("spitzer_icon.png", "der Spitzer", "el sacapuntas", "#1d4ed8"),
        ("buntstift_icon.png", "der Buntstift", "lápiz color", "#1d4ed8"),
    ]
    story.append(create_visual_vocab_strip(school_visuals[:6], cols=6))
    story.append(Spacer(1, 1))
    story.append(create_visual_vocab_strip(school_visuals[6:], cols=4))
    story.append(Spacer(1, 2))

    story.append(Paragraph("<b>Fragen / Preguntas:</b>", s_sec_num))
    story.append(Spacer(1, 1))

    story.append(
        create_question_item(
            "1",
            "Welcher Artikel gehört zu 'Bleistift'?",
            "¿Cuál es el artículo de 'Bleistift' (lápiz)?",
            "der Bleistift",
            "die Bleistift",
            "das Bleistift",
        )
    )
    story.append(Spacer(1, 1))
    story.append(
        create_question_item(
            "2",
            "Welcher Artikel gehört zu 'Schere'?",
            "¿Cuál es el artículo de 'Schere' (tijera)?",
            "der Schere",
            "die Schere",
            "das Schere",
        )
    )
    story.append(Spacer(1, 1))
    story.append(
        create_question_item(
            "3",
            "Welcher Artikel gehört zu 'Mäppchen'?",
            "¿Cuál es el artículo de 'Mäppchen' (cartuchera)?",
            "der Mäppchen",
            "die Mäppchen",
            "das Mäppchen",
        )
    )
    story.append(Spacer(1, 1))
    story.append(
        create_question_item(
            "4",
            "Welcher Artikel gehört zu 'Lineal'?",
            "¿Cuál es el artículo de 'Lineal' (regla)?",
            "der Lineal",
            "die Lineal",
            "das Lineal",
        )
    )
    story.append(Spacer(1, 1))
    story.append(
        create_question_item(
            "5",
            "In meiner Schultasche ist ______ Bleistift.",
            "En mi mochila hay un lápiz (maskulin).",
            "ein",
            "eine",
            "keine",
        )
    )
    story.append(Spacer(1, 1))
    story.append(
        create_question_item(
            "6",
            "Auf dem Tisch liegt ______ Schere.",
            "Sobre la mesa hay una tijera (feminin).",
            "ein",
            "eine",
            "kein",
        )
    )
    story.append(Spacer(1, 1))
    story.append(
        create_question_item(
            "7",
            "Das ist ______ Schere, das ist ein Lineal!",
            "¡Eso no es una tijera, es una regla!",
            "kein",
            "keine",
            "ein",
        )
    )
    story.append(Spacer(1, 2))
    story.append(Paragraph("<b>Punkte / Puntaje: ______ / 10</b>", s_points))

    story.append(PageBreak())

    # =========================================================================
    # PAGE 4: Bauernhoftiere & Adjektive MIT BILDERN
    # =========================================================================
    story.append(
        create_page_top(
            "Animales de la granja y adjetivos",
            "DEUTSCH 3° GRADO",
            "Pebble & Flutter",
            "pebble.png",
            4,
        )
    )
    story.append(Spacer(1, 2))

    story.append(
        create_consigna_block(
            "5",
            "Bauernhoftiere & Adjektive – Animales de la granja con imágenes",
            "Schau dir die Tiere an und kreuze die richtige Antwort über Tiere und Adjektive an.",
            "Mirá las imágenes de los animales y marcá con una X la opción correcta.",
        )
    )
    story.append(Spacer(1, 2))

    animals_visuals = [
        ("hund_icon.png", "der Hund", "el perro", "#1d4ed8"),
        ("katze_icon.png", "die Katze", "el gato", "#b91c1c"),
        ("kuh_icon.png", "die Kuh", "la vaca", "#b91c1c"),
        ("pferd_icon.png", "das Pferd", "el caballo", "#15803d"),
        ("schwein_icon.png", "das Schwein", "el cerdo", "#15803d"),
        ("schaf_icon.png", "das Schaf", "la oveja", "#15803d"),
    ]
    story.append(create_visual_vocab_strip(animals_visuals, cols=6))
    story.append(Spacer(1, 1))

    # Visual strip of key adjectives & opposites with icons
    adjectives_visuals = [
        ("gross_icon.png", "groß", "grande", "#7e22ce"),
        ("klein_icon.png", "klein", "pequeño", "#7e22ce"),
        ("schnell_icon.png", "schnell", "rápido", "#b45309"),
        ("langsam_icon.png", "langsam", "lento", "#b45309"),
        ("lustig_icon.png", "lustig", "divertido", "#15803d"),
        ("bunt_icon.png", "bunt", "colorido", "#ec4899"),
    ]
    story.append(create_visual_vocab_strip(adjectives_visuals, cols=6))
    story.append(Spacer(1, 2))

    story.append(Paragraph("<b>Fragen / Preguntas:</b>", s_sec_num))
    story.append(Spacer(1, 1))

    story.append(
        create_question_item(
            "1",
            "Welcher Artikel gehört zu 'Kuh'?",
            "¿Cuál es el artículo de 'Kuh' (vaca)?",
            "der Kuh",
            "die Kuh",
            "das Kuh",
        )
    )
    story.append(Spacer(1, 1))
    story.append(
        create_question_item(
            "2",
            "Welcher Artikel gehört zu 'Pferd'?",
            "¿Cuál es el artículo de 'Pferd' (caballo)?",
            "der Pferd",
            "die Pferd",
            "das Pferd",
        )
    )
    story.append(Spacer(1, 1))
    story.append(
        create_question_item(
            "3",
            "Welches Tier ist Pebble in Dandy's World?",
            "¿Qué animal es Pebble en Dandy's World?",
            "die Katze",
            "der Hund",
            "das Schwein",
        )
    )
    story.append(Spacer(1, 1))
    story.append(
        create_question_item(
            "4",
            "Das Pferd rennt nicht langsam, es ist sehr...",
            "El caballo no corre lento, es muy...",
            "müde",
            "langsam",
            "schnell (rápido)",
        )
    )
    story.append(Spacer(1, 1))
    story.append(
        create_question_item(
            "5",
            "Die Maus ist klein, aber die Kuh ist...",
            "El ratón es pequeño, pero la vaca es...",
            "groß (grande)",
            "klein",
            "blau",
        )
    )
    story.append(Spacer(1, 1))
    story.append(
        create_question_item(
            "6",
            "Welches Tier gibt uns frische Milch?",
            "¿Qué animal nos da leche fresca?",
            "der Hund",
            "die Kuh",
            "die Katze",
        )
    )
    story.append(Spacer(1, 1))
    story.append(
        create_question_item(
            "7",
            "Flutter hat viele schöne Farben, Flutter ist...",
            "Flutter tiene muchos colores lindos, es...",
            "schwarz",
            "bunt (colorido)",
            "traurig",
        )
    )
    story.append(Spacer(1, 2))
    story.append(Paragraph("<b>Punkte / Puntaje: ______ / 10</b>", s_points))

    story.append(PageBreak())

    # =========================================================================
    # PAGE 5: Familie, Hobbys, Datum & Glosario
    # =========================================================================
    story.append(
        create_page_top(
            "Familia, Hobbies, la fecha y ayudita",
            "DEUTSCH 3° GRADO",
            "Sprout & Astro",
            "sprout.png",
            5,
        )
    )
    story.append(Spacer(1, 2))

    story.append(
        create_consigna_block(
            "6",
            "Familie, Hobbys & Datum – Vocabulario visual",
            "Schau dir die Familie und Hobbys an und wähle die richtige Antwort.",
            "Mirá las imágenes de la familia y pasatiempos y marcá la opción correcta.",
        )
    )
    story.append(Spacer(1, 2))

    fam_hobby_visuals = [
        ("vater_icon.png", "der Vater", "el papá", "#1d4ed8"),
        ("mutter_icon.png", "die Mutter", "la mamá", "#b91c1c"),
        ("bruder_icon.png", "der Bruder", "el hermano", "#1d4ed8"),
        ("schwester_icon.png", "die Schwester", "la hermana", "#b91c1c"),
        ("fussball_icon.png", "Fußball spielen", "jugar fútbol", "#b45309"),
        ("schwimmen_icon.png", "schwimmen", "nadar", "#b45309"),
        ("malen_icon.png", "malen", "dibujar/pintar", "#b45309"),
        ("lesen_icon.png", "lesen", "leer libros", "#b45309"),
    ]
    story.append(create_visual_vocab_strip(fam_hobby_visuals[:4], cols=4))
    story.append(Spacer(1, 1))
    story.append(create_visual_vocab_strip(fam_hobby_visuals[4:], cols=4))
    story.append(Spacer(1, 2))

    story.append(Paragraph("<b>Fragen / Preguntas:</b>", s_sec_num))
    story.append(Spacer(1, 1))

    story.append(
        create_question_item(
            "1",
            "Welcher Tag ist der Prüfungstag von Frau Mónica?",
            "¿Qué día es el examen integrador de la seño Mónica?",
            "Dienstag",
            "Donnerstag (19. Nov.)",
            "Samstag",
        )
    )
    story.append(Spacer(1, 1))
    story.append(
        create_question_item(
            "2",
            "Wie schreibt man das heutige Datum?",
            "¿Cómo se escribe la fecha de hoy?",
            "Donnerstag, der 19. November",
            "Montag, der 3. Mai",
            "Sonntag, der 10. Juli",
        )
    )
    story.append(Spacer(1, 1))
    story.append(
        create_question_item(
            "3",
            "Was machst du gern? — Ich spiele gern ______ (fútbol).",
            "¿Qué te gusta hacer? — Me gusta jugar al...",
            "Fußball",
            "Buch",
            "Schere",
        )
    )
    story.append(Spacer(1, 1))
    story.append(
        create_question_item(
            "4",
            "Astro nimmt ein Buch. Er ______ gern (leer).",
            "Astro agarra un libro. A él le gusta...",
            "schwimmt",
            "schläft",
            "liest",
        )
    )
    story.append(Spacer(1, 2))

    # Glosario Bilingüe: Kleine Hilfe – Ayudita de vocabulario
    story.append(Paragraph("<b>Kleine Hilfe – Ayudita rápida:</b>", s_sec_num))
    story.append(Spacer(1, 1))

    glosario_data = [
        [
            Paragraph("<b>Deutsch</b>", s_q_de),
            Paragraph("<b>Español</b>", s_q_de),
            Paragraph("<b>Deutsch</b>", s_q_de),
            Paragraph("<b>Español</b>", s_q_de),
        ],
        [
            Paragraph("Ich heiße...", s_normal),
            Paragraph("Me llamo...", s_q_es),
            Paragraph("groß / klein", s_normal),
            Paragraph("grande / chico", s_q_es),
        ],
        [
            Paragraph("Ich bin ... Jahre alt.", s_normal),
            Paragraph("Tengo ... años.", s_q_es),
            Paragraph("schnell / langsam", s_normal),
            Paragraph("rápido / lento", s_q_es),
        ],
        [
            Paragraph("Ich habe...", s_normal),
            Paragraph("Tengo...", s_q_es),
            Paragraph("der Opa / die Oma", s_normal),
            Paragraph("el abuelo / la abuela", s_q_es),
        ],
        [
            Paragraph("Mein Lieblingstier...", s_normal),
            Paragraph("Mi animal favorito...", s_q_es),
            Paragraph("Heute ist Donnerstag...", s_normal),
            Paragraph("Hoy es jueves...", s_q_es),
        ],
    ]
    t_glos = Table(glosario_data, colWidths=[130, 135, 135, CONTENT_WIDTH - 400])
    t_glos.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#e2e8f0")),
                ("GRID", (0, 0), (-1, -1), 0.5, C_BOX_BORDER),
                ("TOPPADDING", (0, 0), (-1, -1), 1.5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 1.5),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    story.append(t_glos)
    story.append(Spacer(1, 2))

    # Certificado Final
    cert_data = [
        [
            Paragraph(
                "<para align='center'><font size='9' color='#15803d'><b>🏆 HERZLICHEN GLÜCKWUNSCH, SOFÍA! 🏆</b></font><br/>"
                "<font size='7.5' color='#166534'><b>Du bist ein echter Dandy's World Deutsch-Superstar!</b><br/>"
                "Bereit für den <b>Donnerstag, 19. November</b> mit <b>Frau Mónica Briesemeister</b>! ⭐ 🌟 🌸</font></para>",
                s_top_header,
            )
        ]
    ]
    t_cert = Table(cert_data, colWidths=[CONTENT_WIDTH])
    t_cert.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#dcfce7")),
                ("BOX", (0, 0), (-1, -1), 1, C_GREEN),
                ("ROUNDEDCORNERS", [5, 5, 5, 5]),
                ("TOPPADDING", (0, 0), (-1, -1), 2),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
            ]
        )
    )
    story.append(t_cert)

    doc.build(story)
    print("Visual German PDF built successfully at:", OUTPUT_PDF)


if __name__ == "__main__":
    build_pdf()
