from django.shortcuts import render

import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
import seaborn as sns

def index(request):

    #cargar data sets de seaborn
    tips=sns.load_dataset('tips')
    iris=sns.load_dataset('iris')
    
    
    plt.figure(figsize=(8, 5))
    sns.lineplot(data=tips, x='size', y='total_bill', marker='o')
    plt.title('Gráfica de Líneas: Tamaño de Mesa vs Total Factura')
    plt.tight_layout()
    line_chart = save_chart_to_base64()

    # 3. Gráfica de barras
    plt.figure(figsize=(8, 5))
    sns.barplot(data=tips, x='day', y='total_bill', ci='sd', palette='muted')
    plt.title('Gráfica de Barras: Facturación por Día')
    plt.tight_layout()
    bar_chart = save_chart_to_base64()

    # 4. Gráfica de dispersión
    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=iris, x='sepal_length', y='sepal_width', hue='species', palette='deep')
    plt.title('Gráfica de Dispersión: Longitud vs Anchura de Sépalo')
    plt.tight_layout()
    scatter_chart = save_chart_to_base64()
    #Gráfica de pastel (usando Matplotlib)
    plt.figure(figsize=(8, 5))
    tips['day'].value_counts().plot.pie(autopct='%1.1f%%', colors=sns.color_palette('pastel'))
    plt.title('Gráfica de Pastel: Distribución de Días')
    plt.ylabel('')  # Oculta la etiqueta del eje Y
    plt.tight_layout()
    pie_chart = save_chart_to_base64()

    # 6. Gráfica de histograma
    plt.figure(figsize=(8, 5))
    sns.histplot(data=tips, x='total_bill', bins=20, kde=True, color='purple')
    plt.title('Histograma: Distribución del Total Facturado')
    plt.tight_layout()
    histogram_chart = save_chart_to_base64()

    # 7. Gráfica de cajas (boxplot)
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=tips, x='day', y='total_bill', palette='Set2')
    plt.title('Gráfica de Cajas: Facturación por Día')
    plt.tight_layout()
    boxplot_chart = save_chart_to_base64()

    # 8. Renderizar todas las gráficas en el HTML
    context = {
        'line_chart': line_chart,
        'bar_chart': bar_chart,
        'scatter_chart': scatter_chart,
        'pie_chart': pie_chart,
        'histogram_chart': histogram_chart,
        'boxplot_chart': boxplot_chart,
    }



    return render(request, 'grafica/index.html',context)

def save_chart_to_base64():
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    return base64.b64encode(image_png).decode('utf-8')