const data = [{name: "Positive", value: 150}, {name: "Negative", value: 105}]

const svg = d3.select('svg'),
    width = svg.attr('width'),
    height = svg.attr('height');

const radius = 200;
const g = svg.append('g').attr('transform', `translate(${width/2}, ${height/2})`);

const color = d3.scaleOrdinal(['#0AB97F', '#E0235D']);

const pie = d3.pie().value(d => d.value);

const path = d3.arc().outerRadius(radius).innerRadius(100);

const pies = g.selectAll('.arc').data(pie(data)).enter().append('g').attr('class', 'arc');

pies.append('path').attr('d', path).attr('fill', d => color(d.data.value)).attr(d.data.name);


pies.append('text').text("Positive").attr('transform', `translate(10, ${height/2})`)