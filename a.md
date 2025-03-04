### Análisis del Modelo de Regresión OLS

El modelo de regresión lineal ajustado tiene como variable dependiente FinalRaceTime y utiliza las siguientes variables predictoras:

- MaxSpeed
- Age
- FinalPosition
- Points
- Overtakes
- TyreWear
- WeatherCondition_Mixed
- TrackGrip_Low

#### Evaluación General del Modelo

- $R^2$ = 0.911 -> Indica que el 91.1% de la variabilidad en el `FinalRaceTime` puede ser explicada por las variables predictoras del modelo.
- $R^2$ ajustado = 0.880 -> Penaliza el $R^2$  por el número de predictores. Aunque es menor, sigue siendo alto, lo que sugiere un buen ajuste del modelo.

El modelo explica una gran parte de la variabilidad en los tiempos de carrera. Un

$R^2$ mayor a 0.8 sugiere un buen modelo en términos de ajuste.

#### Significancia Global del Modelo

``Prueba F-Statistic`` : prueba estadística utilizada para evaluar la **significancia global** del modelo de regresión. Responde a las pregunta:

> ¿Al menos una de las variables predictoras tiene un efecto significativo sobre la variable dependiente?

- F = 29.53 con p-value = 2.52e-10
- Esto indica que al menos una de las variables predictoras tiene un impacto significativo en FinalRaceTime.

#### Análisis de los Coeficientes y Significancia Individual

Cada coeficiente indica cuánto cambia FinalRaceTime cuando la variable predictora aumenta en una unidad, manteniendo las demás constantes.

| Variable                    | Coeficiente | p-valor | Interpretacion                                                                                                                 |
| --------------------------- | ----------- | ------- | ------------------------------------------------------------------------------------------------------------------------------ |
| Intercept (Constante)       | 267.70      | 0.000   | Tiempo base sin efectos de las variables predictoras                                                                           |
| MaxSpeed (x1)               | -3.85       | 0.000   | A mayor velocidad máxima, menor tiempo de carrera                                                                             |
| Age (x2)                    | -2.59       | 0.001   | A mayor edad, menor tiempo de carrera (pilotos más experimentados pueden ser más rápidos)                                   |
| FinalPosition (x3)          | 13.95       | 0.000   | A medida que la posición final aumenta, el tiempo de carrera es mayor (pilotos más lentos terminan en posiciones más bajas) |
| Points (x4)                 | 8.88        | 0.000   |                                                                                                                                |
| Overtakes (x5)              | -2.77       | 0.008   | Más adelantamientos reducen el tiempo de carrera (pilotos agresivos ganan tiempo)                                             |
| TyreWear (x6)               | -5.28       | 0.000   | Más desgaste de neumáticos, menor tiempo (posiblemente estrategia agresiva con neumáticos blandos)                          |
| WeatherCondition_Mixed (x7) | 4.24        | 0.000   | Condiciones climáticas mixtas aumentan el tiempo de carrera                                                                   |
| TrackGrip_Low (x8)          | 4.50        | 0.000   | Bajo agarre de pista aumenta el tiempo de carrera                                                                              |


**Conclusión:**

- Todos los **p-valores** son  **< 0.05** , lo que significa que  **todas las variables son significativas** .
- Los signos de los coeficientes tienen  **interpretaciones lógicas** , lo que refuerza la validez del modelo.
- El modelo parece ser  **robusto y bien especificado** .


## **Conclusión Final**

✅  **El modelo es sólido** , con un  **buen ajuste (R2=91.1R^2 = 91.1%**R**2**=**91.1)** , **predictores significativos** y  **una interpretación lógica de los coeficientes** .

📌  **Próximos Pasos** :

Antes de concluir la investigación, es importante validar los **supuestos del modelo** (normalidad, homoscedasticidad, independencia y multicolinealidad). Esto asegurará que los resultados sean confiables. 🚀
