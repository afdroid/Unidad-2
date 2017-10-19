from flask import Flask, render_template, redirect, request
from calculobruto import utilidad_bruta, perdida_bruta

app = Flask(__name__)


@app.route('/')
def heome() -> '302':
    return redirect('/entry')

@app.route('/calculobruto', methods=['POST'])
def calculate1() -> 'html':
    ven_net = float(request.form['ven_net'])
    cost_ven = float(request.form['cost_ven'])
    title = 'Aqui estan sus resultados'
    results = float(utilidad_bruta(ven_net, cost_ven))
    return render_template('results.html',
                           the_title=title,
                           the_vent_net=ven_net,
                           the_cost_vent=cost_ven,
                           the_results=results,)


@app.route('/calculobruto2', methods=['POST'])
def calculate2() -> 'html':
    cost_venM = float(request.form['cost_venM'])
    ven_nets= float(request.form['ven_nets'])
    title = 'Aqui estan sus resultados'
    results = float(perdida_bruta(cost_venM, ven_nets))
    return render_template('results2.html',
                           the_title=title,
                           the_cost_vent=cost_venM,
                           the_vent_net=ven_nets,
                           the_results=results,)


@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Bienvenido al calculo de valores brutos')


@app.route('/utilidad')
def entry_page1() -> 'html':
    return render_template('utilidadbruta.html', the_title='Bienvenido al calculo de Utilidades Brutas')


@app.route('/perdida')
def entry_page2() -> 'html':
    return render_template('perdidabruta.html', the_title='Bienvenido al calculo de Perdidas Brutas')


app.run(debug=True)
