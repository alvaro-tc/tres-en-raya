#set page(width: 33.87cm, height: 19.05cm, margin: 1.5cm)
#set text(size: 18pt, lang: "es")
#show heading.where(level: 1): it => [#set text(26pt, fill: rgb("#1f4e79")); #it]
#let slide(t, body) = { pagebreak(weak: true); heading(level: 1, t); v(0.3cm); body }

#align(center + horizon)[
  #text(32pt, weight: "bold", fill: rgb("#1f4e79"))[Kata Tres en Raya] \
  #text(22pt)[Pruebas unitarias propias vs. generadas por IA] \
  #v(1cm) Python · unittest · TDD
]

#slide("Alcance")[
  - Programa: clase `TresEnRaya` con `jugar(fila, col)`.
  - Reglas: X inicia, turnos alternos, sin jugar fuera/ocupado, gana 3 en línea, empate, fin de partida.
  - *Propias*: 13 pruebas (`tests/`). *IA*: 22 pruebas (`ia/`), generadas solo con el prompt (`ia/prompt.md`).
  - Resultado: ambos conjuntos pasan sobre el mismo programa.
]

#slide("Prompt usado")[
  Se entregó a la IA: reglas numeradas, API (`jugar`, `tablero`, `turno`, `ganador`), requisitos de estilo (nombres descriptivos en español, un caso por test, casos borde, sin dependencias).

  #v(0.5cm)
  La IA *no vio* el código del programa ni mis pruebas: solo el prompt.
]

#slide("Comparación general")[
  #table(columns: (auto, 1fr, 1fr), inset: 8pt, stroke: 0.5pt + gray,
    [*Aspecto*], [*Propias*], [*IA*],
    [Nº de tests], [13 (+ `subTest`: 8 líneas)], [22],
    [Organización], [4 clases: Tablero, Turnos, Ganador, Empate], [6 clases por fase del juego],
    [Nombres], [Cortos (`test_empate`)], [Muy descriptivos, largos],
    [Líneas ganadoras], [Las 8, para X, con `subTest` y relleno generado], [4 casos sueltos: fila, columna, 2 diagonales, mezclando X/O],
    [Duplicación], [Helper `jugar_todas`], [Jugadas repetidas a mano en cada test],
    [Casos borde], [Victoria en la 9.ª jugada (no es empate)], [Empate no se declara antes de llenar],
    [Estado inicial], [Solo tablero vacío], [Tablero, turno y ganador separados],
  )
]

#slide("Diferencias sustanciales")[
  + *Cobertura de victorias*: las propias cubren las 8 líneas; la IA solo 4 (una por tipo). Un error en, p. ej., la fila 3 pasaría desapercibido.
  + *Caso borde clave*: la IA no probó que ganar con la 9.ª jugada devuelve el ganador y no `"Empate"`; las propias sí.
  + *Granularidad*: la IA separa más aserciones (más tests, más legibles al fallar); las propias son más compactas.
  + *Mantenibilidad*: las propias usan helper y `subTest`; la IA repite código (más ruido).
  + *Supuestos*: la IA asumió detalles no especificados (`turno` = jugador siguiente, índice `fila*3+col`); además, un comentario suyo del tablero de empate no coincide con las jugadas reales.
  + *Estado inicial/turno*: la IA verifica más atributos (`turno`, `ganador`) y devuelve `None` en curso.
]

#slide("Conclusiones")[
  - La IA entrega rápido una suite amplia y legible, pero con cobertura superficial de combinaciones y comentarios incorrectos: *requiere revisión humana*.
  - Las pruebas propias son más exhaustivas en lo crítico (todas las líneas, límite de la 9.ª jugada) y menos repetitivas.
  - Mejor resultado: partir de la suite de IA para estructura y completar con casos borde propios.
  - Repositorio: https://github.com/alvaro-tc/tres-en-raya
]
