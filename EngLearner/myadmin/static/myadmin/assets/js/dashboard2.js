$(function() {
	'use strict';
	var options = {
		chart: {
			type: "area",
			height: 300,
			foreColor: "#838ab6",
			scroller: {
				enabled: false,
				track: {
					height: 7,
					background: '#838ab6'
				},
				thumb: {
					height: 10,
					background: '#838ab6'
				},
				scrollButtons: {
					enabled: false,
					size: 9,
					borderWidth: 1,
					borderColor: '#838ab6',
					fillColor: '#838ab6'
				},
				padding: {
					left: 30,
					right: 20
				}
			},
			stacked: true,
			dropShadow: {
				enabled: false,
				enabledSeries: [0],
				top: -2,
				left: 2,
				blur: 5,
				opacity: 0.06
			}
		},
		colors: ['#f47b25', '#5d61bf' ],
		stroke: {
			curve: "smooth",
			width: 3
		},
		dataLabels: {
			enabled: false
		},
		series: [{
			name: 'Total Views',
			data: data
		}],
		markers: {
			size: 0,
			strokeColor: "#838ab6",
			strokeWidth: 3,
			strokeOpacity: 1,
			fillOpacity: 1,
			hover: {
				size: 6
			}
		},
		xaxis: {
			type: "datetime",
			axisBorder: {
				show: false
			},
			axisTicks: {
				show: false
			}
		},
		yaxis: {
			tickAmount: 4,
			min: 0,
			labels: {
				offsetX: 24,
				offsetY: -5
			},
			tooltip: {
				enabled: false
			}
		},
		grid: {
			padding: {
				left: -5,
				right: 5
			}
		},
		tooltip: {
			x: {
				format: "yyyy MMM dd"
			},
		},
		legend: {
			position: 'top',
			horizontalAlign: 'left'
		},
		fill: {
			type: "solid",
			fillOpacity: 0.7
		}
	};
	
	/*----ApexCharts----*/
	var chart = new ApexCharts(document.querySelector("#timeline-chart"), options);
	chart.render();
});
