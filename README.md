# TRABAJO FIN DE GRADO: MODELADO DE MÓDULO TRANSLÚCIDO DE CONCENTRACIÓN FOTOVOLTAICA PARA ILUMINACIÓN EN EDIFICIOS. 


[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/AnaDue99/microCPV_Iluminacion/HEAD)



La concentración fotovoltaica es una tecnología de generación de energía renovable que data de los años 70. A pesar de obtener grandes rendimientos energéticos, económicamente hablando no es competitiva con las tecnologías más comunes de generación fotovoltaica. Por ello, el uso de esta tecnología ha de ser justificado para casos concretos en los que añada cierto valor. En este Trabajo de Fin de Grado se va a estudiar la viabilidad de su uso para la iluminación de estancias estudiando un módulo de concentración transparente con tracking integrado. Los módulos CPV o concentradores fotovoltaicos, utilizan lentes para enfocar la luz en células fotovoltaicas de mayor rendimiento que las células de silicio comúnmente utilizadas.

Con esta propuesta se busca justificar el uso de la tecnología de concentración fotovoltaica como fotovoltaica integrada en edificios. En específico, se va a tratar de optimizar la tecnología para la iluminación de una estancia y a su vez analizar la energía fotovoltaica que se puede generar.

En el entorno de programación Python y con la librería pvlib se modela la magnitud lumínica que la tecnología es capaz de emitir en base a varios elementos: ángulo de incidencia, irradiancia entrante, distribución espectral y posición de la célula fotovoltaica dentro de la unidad célula-lente. Este último es la característica más importante de la tecnología de cara a este proyecto y a su control se le denomina tracking interno. Este tracking interno normalmente es usado para conseguir la máxima generación fotovoltaica, sin embargo, en este trabajo se va a controlar para una emisión lumínica constante. Es decir, el enfoque de la irradiación entrante a la lente se dividirá tanto para iluminación (valor constante de luz emitida) como para generar energía fotovoltaica (valor variable de luz concentrada sobre la célula fotovoltaica).

En el proyecto se propone un caso de estudio de una luminaria formada por un módulo de concentración y se evalúa la distribución lumínica de esta en el entorno de modelado lumínico DIAlux. En este caso se tiene en cuenta la norma europea para la iluminación de interiores UNE 12464.
