const express = require('express');
fs = require('fs');
const app = express();
const port = process.env.PORT || 4040;
app.listen(port);
app.set('view engine', 'ejs'); 
app.use(express.static(__dirname + '/public'));







app.get('/',(req,res) => {

    let output_data;
    fs.readFile('../output.txt', 'utf8', function (err,data) {
        if (err) {
        return console.log(err);
        }
        output_data  = data.split('\n');

        data = {};
        let colors = ['#228B22','#6495ED','#D2691E','#FF7F50','#BDB76B']
        let ct=0;
        let total = 0;
        let mini = Number.MAX_VALUE
        let maxi = -1
        for(var i=0;i<output_data.length;i++)
        {
            if(output_data[i][output_data[i].length-1]==':')
                {
                    if(total!=0)
                    {
                        for(let j=0;j<data[testcase].length;j++)
                            data[testcase][j]['total'] = total;
                    }
                    if(maxi!=-1)
                    {
                        data[testcase]['mini'] = mini
                        data[testcase]['maxi'] = maxi
                    }
                    data[output_data[i]] = []
                    testcase = output_data[i];
                    total = 0;
                    ct = 0;
                    mini = Number.MAX_VALUE
                    maxi = -1
                }
            else if(output_data[i].length>1)
                {
                    data[testcase].push({sort:output_data[i].split(':')[0],time:parseFloat(output_data[i].split(':')[1].slice(1).replace('s','')),color:colors[ct]})
                    ct ++;
                    let nr = parseFloat(output_data[i].split(':')[1].replace('s',''));
                    total += nr;
                    if(nr<mini && nr!=0)
                        mini = nr;
                    if(nr>maxi && nr!=0)
                        maxi = nr;
                }
        }

        if(total!=0)
        {
            for(let j=0;j<data[testcase].length;j++)
                data[testcase][j]['total'] = total;
        }
        if(maxi!=-1)
        {
            data[testcase]['mini'] = mini
            data[testcase]['maxi'] = maxi
        }
        res.render('index',{data:data});
    });

    
})


app.get('/view_testcase',(req,res) => {
    testcase = req.query.testcase.toLowerCase().replace(':','')

    let output_data;
    fs.readFile('../Testcases/'+testcase+'.txt', 'utf8', function (err,data) {
        if (err) {
        return console.log(err);
        }
        res.send(data)
    });

    
})