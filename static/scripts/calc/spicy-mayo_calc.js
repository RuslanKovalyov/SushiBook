function writ() {
    tbl = document.getElementById('tbl');
    main_ingredient = Math.round(document.getElementById("myNumber").value);

    for (var i = tbl.rows.length; i > 0; i--) {
        tbl.deleteRow(0);
    }

    addRow(tbl, 'Kewpie mayo', Math.round(main_ingredient) + ' ml', Math.round(main_ingredient) / 1000 + ' liter', Math.round(main_ingredient) / 250 + ' cup');
    addRow(tbl, 'sriracha', Math.round(main_ingredient / 5) + ' ml', Math.round(main_ingredient / 5)  / 1000 + ' liter', Math.round(main_ingredient / 5)  / 250 + ' cup');
    addRow(tbl, 'sweet chili', Math.round(main_ingredient / 10) + ' ml', Math.round(main_ingredient / 10) / 1000 + ' liter', Math.round(main_ingredient / 10) / 250 + ' cup');
    addRow(tbl, 'Chili oil', Math.round(main_ingredient / 20) + ' ml', Math.round(main_ingredient / 20) / 1000 + ' liter', Math.round(main_ingredient / 20) / 250 + ' cup');
    addRow(tbl, 'Togarashi', Math.round(main_ingredient / 30) + ' gr', Math.round(main_ingredient / 30) / 1000 + ' kg', Math.round(main_ingredient / 30) / 250 + ' cup');
    addRow(tbl, 'Yuzu juice ', Math.round(main_ingredient / 20) + ' ml', Math.round(main_ingredient / 20) / 1000 + ' liter', Math.round(main_ingredient / 20) / 250 + ' cup');
    addRow(tbl, 'Sesame oil ', Math.round(main_ingredient / 20) + ' ml', Math.round(main_ingredient / 20) / 1000 + ' liter', Math.round(main_ingredient / 20) / 250 + ' cup');
    addRow(tbl, 'Tobiko', Math.round(main_ingredient / 20) + ' gr', Math.round(main_ingredient / 20) / 1000 + ' kg', Math.round(main_ingredient / 20 ) / 250 + 'cup');

}

function addCell(tr, val) {
    var td = document.createElement('td');
    td.innerHTML = val;
    tr.appendChild(td)
}

function addRow(tbl, val_1, val_2, val_3, val_4) {
    var tr = document.createElement('tr');
    addCell(tr, val_1);
    addCell(tr, val_2);
    addCell(tr, val_3);
    addCell(tr, val_4);
    tbl.appendChild(tr)
}