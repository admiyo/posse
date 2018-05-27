
// list of countries, defined with JavaScript object literals
var data = [
    {"name": "Sweden"}, {"name": "China"}, {"name": "Peru"}, {"name": "Czech Republic"},
    {"name": "Bolivia"}, {"name": "Latvia"}, {"name": "Samoa"}, {"name": "Armenia"},
    {"name": "Greenland"}, {"name": "Cuba"}, {"name": "Western Sahara"}, {"name": "Ethiopia"},
    {"name": "Malaysia"}, {"name": "Argentina"}, {"name": "Uganda"}, {"name": "Chile"},
    {"name": "Aruba"}, {"name": "Japan"}, {"name": "Trinidad and Tobago"}, {"name": "Italy"},
    {"name": "Cambodia"}, {"name": "Iceland"}, {"name": "Dominican Republic"}, {"name": "Turkey"},
    {"name": "Spain"}, {"name": "Poland"}, {"name": "Haiti"}
];



function doFetch() {
    var services = []
    fetch("http://127.0.0.1:5000/services")
        .then(res => res.json())
        .then(
            (result) => {
                services = result
            },
            // Note: it's important to handle errors here
            // instead of a catch() block so that we don't swallow
            // exceptions from actual bugs in components.
            (error) => {
                
            }
        )
    return services
};


var services = doFetch();

const e = React.createElement;
var DynamicSearch = React.createClass({

    // sets initial state
    getInitialState: function(){
        return { searchString: '',
                 
               };
    },

    // sets state, triggers render method
    handleChange: function(event){
        
        // grab value form input box
        this.setState({searchString:event.target.value});
        console.log("scope updated!");
    },

    render: function() {
        var services = this.props.items;
        var searchString = this.state.searchString.trim().toLowerCase();

        // filter services list by value from input box
        if (searchString.length > 0) {
            services = services.filter(function (service) {
                return service.type.toLowerCase().match(searchString);
            });
        }

        return React.createElement(
            "div",
            null,
            React.createElement("input", { type: "text", value: this.state.searchString, onChange: this.handleChange, placeholder: "Search!" }),
            React.createElement(
                "table",
                null,
                React.createElement(
                    "thead",
                    null,
                    React.createElement(
                        "tr",
                        null,
                        React.createElement(
                            "th",
                            null,
                            "Service"
                        ),
                        React.createElement(
                            "th",
                            null,
                            "action"
                        ),
                        React.createElement(
                            "th",
                            null,
                            "path"
                        ),
                        React.createElement(
                            "th",
                            null,
                            "scope"
                        ),
                        React.createElement(
                            "th",
                            null,
                            "role"
                        )
                    )
                ),
                React.createElement(
                    "tbody",
                    null,
                    services.map(function (service) {
                        return React.createElement(
                            "tr",
                            null,
                            React.createElement(
                                "td",
                                null,
                                "type"
                            ),
                            React.createElement(
                                "td",
                                null,
                                "action"
                            ),
                            React.createElement(
                                "td",
                                null,
                                "path"
                            ),
                            React.createElement(
                                "td",
                                null,
                                "scope"
                            ),
                            React.createElement(
                                "td",
                                null,
                                service.type
                            )
                        );
                    })
                )
            )
        );
    },




});

ReactDOM.render(
    React.createElement(DynamicSearch, {items: services}, null),
    document.getElementById('searchtool')
);

