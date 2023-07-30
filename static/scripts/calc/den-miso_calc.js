function writ() {
    tbl = document.getElementById('tbl');
    main_ingredient = Math.round(document.getElementById("myNumber").value);

    for (var i = tbl.rows.length; i > 0; i--) {
        tbl.deleteRow(0);
    }
    m = main_ingredient;
    Mirin = main_ingredient / 200 * 70;
    Sake = main_ingredient / 200 * 70;
    Sugar = main_ingredient / 2;

    addRow(tbl, 'Shiro Miso', Math.round(m) + ' gr', Math.round(m) / 1000 + ' liter', Math.round(m) / 250 + ' cup');
    addRow(tbl, 'Mirin', Math.round(Mirin) + ' ml', Math.round(Mirin) / 1000 + ' liter', Math.round(Mirin) / 250 + ' cup');
    addRow(tbl, 'Sake', Math.round(Sake) + ' ml', Math.round(Sake) / 1000 + ' liter', Math.round(Sake) / 250 + ' cup');
    addRow(tbl, 'Sugar', Math.round(Sugar) + ' gr', Math.round(Sugar) / 1000 + ' kg', Math.round(Sugar) / 250 + ' cup');

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