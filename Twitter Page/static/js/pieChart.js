//test data
const data = [{name: "Positive", value: 150}, {name: "Negative", value: 105}]

//get dimensions
const svg = d3.select('svg'),
    width = svg.attr('width'),
    height = svg.attr('height');

const radius = 175;
const g = svg.append('g').attr('transform', `translate(${width/2}, ${height/2})`);

//enter colors
const color = d3.scaleOrdinal(['#0AB97F', '#E0235D']);

//make pie chart
const pie = d3.pie().value(d => d.value);

const path = d3.arc().outerRadius(radius).innerRadius(80);

const label = d3.arc().outerRadius(radius).innerRadius(radius-95);

const pieces = g.selectAll('.arc').data(pie(data)).enter().append('g').attr('class', 'arc');

pieces.append('path').attr('d', path).attr('fill', d => color(d.data.value));

pieces.append('text')
    .attr('transform', function(d) {
        return `translate(${label.centroid(d)})`;})
    .attr("dy", ".35em")
    .style("text-anchor", "middle")
    .attr("fill", "#fff")
    .text(d => d.data.name)