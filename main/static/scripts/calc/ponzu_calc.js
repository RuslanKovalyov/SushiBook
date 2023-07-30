function writ() {
    tbl = document.getElementById('tbl');
    main_ingredient = Math.round(document.getElementById("myNumber").value);

    for (var i = tbl.rows.length; i > 0; i--) {
        tbl.deleteRow(0);
    }

    addRow(tbl, 'Soy sauce', Math.round(main_ingredient) + ' ml', Math.round(main_ingredient) / 1000 + ' liter', Math.round(main_ingredient) / 250 + ' cup');
    addRow(tbl, 'Orange juice', Math.round(main_ingredient / 2) + ' ml', Math.round(main_ingredient / 2)  / 1000 + ' liter', Math.round(main_ingredient / 2)  / 250 + ' cup');
    addRow(tbl, 'Yuzu juice', Math.round(main_ingredient / 100 * 30) + ' ml', Math.round(main_ingredient / 100 * 30) / 1000 + ' liter', Math.round(main_ingredient / 100 * 30) / 250 + ' cup');
    addRow(tbl, 'Lemon juice', Math.round(main_ingredient / 100 * 30) + ' ml', Math.round(main_ingredient / 100 * 30) / 1000 + ' liter', Math.round(main_ingredient / 100 * 30) / 250 + ' cup');
    addRow(tbl, 'Chili oil ', Math.round(main_ingredient / 100 * 15) + ' ml', Math.round(main_ingredient / 100 * 15) / 1000 + ' liter', Math.round(main_ingredient / 100 * 15) / 250 + ' cup');
    addRow(tbl, 'Sesame oil', Math.round(main_ingredient  / 100 * 20) + ' ml', Math.round(main_ingredient / 100 * 20) / 1000 + ' liter', Math.round(main_ingredient / 100 * 20) / 250 + ' cup');
    addRow(tbl, 'Ginger root', Math.round(main_ingredient / 5) + ' gr', Math.round(main_ingredient / 5) / 1000 + ' kg', Math.round(main_ingredient / 1.5 ) / 250 + ' root');

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