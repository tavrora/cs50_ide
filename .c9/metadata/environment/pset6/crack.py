{"filter":false,"title":"crack.py","tooltip":"/pset6/crack.py","ace":{"folds":[],"scrolltop":742.8125,"scrollleft":0,"selection":{"start":{"row":84,"column":0},"end":{"row":84,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"hash":"cbcd22332cc20dc36b97145b1ec2dba87a350f8f","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":43,"column":18},"end":{"row":43,"column":19},"action":"remove","lines":["c"],"id":307},{"start":{"row":43,"column":18},"end":{"row":43,"column":26},"action":"insert","lines":["password"]}],[{"start":{"row":21,"column":4},"end":{"row":21,"column":5},"action":"remove","lines":["c"],"id":308},{"start":{"row":21,"column":4},"end":{"row":21,"column":5},"action":"insert","lines":["p"]}],[{"start":{"row":24,"column":23},"end":{"row":24,"column":24},"action":"remove","lines":["c"],"id":309},{"start":{"row":24,"column":23},"end":{"row":24,"column":24},"action":"insert","lines":["p"]}],[{"start":{"row":28,"column":14},"end":{"row":28,"column":15},"action":"remove","lines":["c"],"id":310},{"start":{"row":28,"column":14},"end":{"row":28,"column":15},"action":"insert","lines":["p"]}],[{"start":{"row":35,"column":0},"end":{"row":35,"column":8},"action":"remove","lines":["        "],"id":311}],[{"start":{"row":30,"column":0},"end":{"row":31,"column":0},"action":"insert","lines":["",""],"id":312}],[{"start":{"row":37,"column":25},"end":{"row":38,"column":0},"action":"insert","lines":["",""],"id":313},{"start":{"row":38,"column":0},"end":{"row":38,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":38,"column":8},"end":{"row":38,"column":10},"action":"insert","lines":["()"],"id":314}],[{"start":{"row":38,"column":9},"end":{"row":38,"column":10},"action":"insert","lines":["p"],"id":315},{"start":{"row":38,"column":10},"end":{"row":38,"column":11},"action":"insert","lines":["r"]},{"start":{"row":38,"column":11},"end":{"row":38,"column":12},"action":"insert","lines":["i"]},{"start":{"row":38,"column":12},"end":{"row":38,"column":13},"action":"insert","lines":["n"]},{"start":{"row":38,"column":13},"end":{"row":38,"column":14},"action":"insert","lines":["t"]}],[{"start":{"row":38,"column":14},"end":{"row":38,"column":15},"action":"remove","lines":[")"],"id":316}],[{"start":{"row":38,"column":8},"end":{"row":38,"column":9},"action":"remove","lines":["("],"id":317}],[{"start":{"row":38,"column":13},"end":{"row":38,"column":15},"action":"insert","lines":["()"],"id":318}],[{"start":{"row":38,"column":14},"end":{"row":38,"column":15},"action":"insert","lines":["p"],"id":319},{"start":{"row":38,"column":15},"end":{"row":38,"column":16},"action":"insert","lines":["a"]},{"start":{"row":38,"column":16},"end":{"row":38,"column":17},"action":"insert","lines":["s"]},{"start":{"row":38,"column":17},"end":{"row":38,"column":18},"action":"insert","lines":["s"]},{"start":{"row":38,"column":18},"end":{"row":38,"column":19},"action":"insert","lines":["w"]},{"start":{"row":38,"column":19},"end":{"row":38,"column":20},"action":"insert","lines":["o"]},{"start":{"row":38,"column":20},"end":{"row":38,"column":21},"action":"insert","lines":["r"]}],[{"start":{"row":38,"column":21},"end":{"row":38,"column":22},"action":"insert","lines":["d"],"id":320}],[{"start":{"row":21,"column":4},"end":{"row":21,"column":5},"action":"remove","lines":["p"],"id":321},{"start":{"row":21,"column":4},"end":{"row":21,"column":5},"action":"insert","lines":["c"]}],[{"start":{"row":28,"column":14},"end":{"row":28,"column":15},"action":"remove","lines":["p"],"id":322},{"start":{"row":28,"column":14},"end":{"row":28,"column":15},"action":"insert","lines":["c"]}],[{"start":{"row":24,"column":23},"end":{"row":24,"column":24},"action":"remove","lines":["p"],"id":323},{"start":{"row":24,"column":23},"end":{"row":24,"column":24},"action":"insert","lines":["c"]}],[{"start":{"row":46,"column":23},"end":{"row":47,"column":0},"action":"insert","lines":["",""],"id":324},{"start":{"row":47,"column":0},"end":{"row":47,"column":12},"action":"insert","lines":["            "]},{"start":{"row":47,"column":12},"end":{"row":48,"column":0},"action":"insert","lines":["",""]},{"start":{"row":48,"column":0},"end":{"row":48,"column":12},"action":"insert","lines":["            "]},{"start":{"row":48,"column":12},"end":{"row":49,"column":0},"action":"insert","lines":["",""]},{"start":{"row":49,"column":0},"end":{"row":49,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":49,"column":8},"end":{"row":49,"column":12},"action":"remove","lines":["    "],"id":325},{"start":{"row":49,"column":4},"end":{"row":49,"column":8},"action":"remove","lines":["    "]},{"start":{"row":49,"column":0},"end":{"row":49,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":49,"column":0},"end":{"row":63,"column":23},"action":"insert","lines":["for c in string.ascii_letters:     # enumeration of all 2 letters","","    # loop to iterate over the next letter","    for c1 in string.ascii_letters:","","        password = c + c1","        print(password)","","        # determine hash","        hash = crypt.crypt(password, salt)","","        # check the match","        if hash == sys.argv[1]:","            print(password)","            sys.exit(0)"],"id":326}],[{"start":{"row":63,"column":23},"end":{"row":64,"column":0},"action":"insert","lines":["",""],"id":327},{"start":{"row":64,"column":0},"end":{"row":64,"column":12},"action":"insert","lines":["            "]},{"start":{"row":64,"column":12},"end":{"row":65,"column":0},"action":"insert","lines":["",""]},{"start":{"row":65,"column":0},"end":{"row":65,"column":12},"action":"insert","lines":["            "]},{"start":{"row":65,"column":12},"end":{"row":66,"column":0},"action":"insert","lines":["",""]},{"start":{"row":66,"column":0},"end":{"row":66,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":66,"column":8},"end":{"row":66,"column":12},"action":"remove","lines":["    "],"id":328},{"start":{"row":66,"column":4},"end":{"row":66,"column":8},"action":"remove","lines":["    "]},{"start":{"row":66,"column":0},"end":{"row":66,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":66,"column":0},"end":{"row":80,"column":23},"action":"insert","lines":["for c in string.ascii_letters:     # enumeration of all 2 letters","","    # loop to iterate over the next letter","    for c1 in string.ascii_letters:","","        password = c + c1","        print(password)","","        # determine hash","        hash = crypt.crypt(password, salt)","","        # check the match","        if hash == sys.argv[1]:","            print(password)","            sys.exit(0)"],"id":329}],[{"start":{"row":68,"column":4},"end":{"row":68,"column":42},"action":"remove","lines":["# loop to iterate over the next letter"],"id":330},{"start":{"row":68,"column":0},"end":{"row":68,"column":4},"action":"remove","lines":["    "]},{"start":{"row":67,"column":0},"end":{"row":68,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":68,"column":35},"end":{"row":69,"column":0},"action":"insert","lines":["",""],"id":331},{"start":{"row":69,"column":0},"end":{"row":69,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":69,"column":8},"end":{"row":70,"column":0},"action":"insert","lines":["",""],"id":332},{"start":{"row":70,"column":0},"end":{"row":70,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":70,"column":8},"end":{"row":70,"column":40},"action":"insert","lines":[" for c1 in string.ascii_letters:"],"id":333}],[{"start":{"row":70,"column":14},"end":{"row":70,"column":15},"action":"remove","lines":["1"],"id":334},{"start":{"row":70,"column":14},"end":{"row":70,"column":15},"action":"insert","lines":["2"]}],[{"start":{"row":72,"column":25},"end":{"row":72,"column":26},"action":"insert","lines":[" "],"id":335},{"start":{"row":72,"column":26},"end":{"row":72,"column":27},"action":"insert","lines":["+"]}],[{"start":{"row":72,"column":27},"end":{"row":72,"column":28},"action":"insert","lines":[" "],"id":336},{"start":{"row":72,"column":28},"end":{"row":72,"column":29},"action":"insert","lines":["c"]},{"start":{"row":72,"column":29},"end":{"row":72,"column":30},"action":"insert","lines":["2"]}],[{"start":{"row":47,"column":0},"end":{"row":47,"column":12},"action":"remove","lines":["            "],"id":337},{"start":{"row":48,"column":0},"end":{"row":48,"column":12},"action":"remove","lines":["            "]},{"start":{"row":64,"column":0},"end":{"row":64,"column":12},"action":"remove","lines":["            "]},{"start":{"row":65,"column":0},"end":{"row":65,"column":12},"action":"remove","lines":["            "]},{"start":{"row":69,"column":0},"end":{"row":69,"column":8},"action":"remove","lines":["        "]}],[{"start":{"row":57,"column":0},"end":{"row":57,"column":24},"action":"remove","lines":["        # determine hash"],"id":338},{"start":{"row":56,"column":0},"end":{"row":57,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":55,"column":0},"end":{"row":55,"column":23},"action":"remove","lines":["        print(password)"],"id":339},{"start":{"row":54,"column":25},"end":{"row":55,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":54,"column":25},"end":{"row":55,"column":0},"action":"remove","lines":["",""],"id":340}],[{"start":{"row":56,"column":0},"end":{"row":57,"column":25},"action":"remove","lines":["","        # check the match"],"id":341},{"start":{"row":55,"column":42},"end":{"row":56,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":53,"column":0},"end":{"row":54,"column":0},"action":"insert","lines":["",""],"id":342}],[{"start":{"row":54,"column":0},"end":{"row":54,"column":4},"action":"insert","lines":["    "],"id":343}],[{"start":{"row":54,"column":4},"end":{"row":54,"column":8},"action":"insert","lines":["    "],"id":344}],[{"start":{"row":54,"column":8},"end":{"row":54,"column":9},"action":"insert","lines":["#"],"id":345}],[{"start":{"row":54,"column":9},"end":{"row":54,"column":10},"action":"insert","lines":[" "],"id":346},{"start":{"row":54,"column":10},"end":{"row":54,"column":11},"action":"insert","lines":["c"]}],[{"start":{"row":54,"column":10},"end":{"row":54,"column":11},"action":"remove","lines":["c"],"id":347}],[{"start":{"row":54,"column":10},"end":{"row":54,"column":11},"action":"insert","lines":["с"],"id":348},{"start":{"row":54,"column":11},"end":{"row":54,"column":12},"action":"insert","lines":["к"]},{"start":{"row":54,"column":12},"end":{"row":54,"column":13},"action":"insert","lines":["л"]},{"start":{"row":54,"column":13},"end":{"row":54,"column":14},"action":"insert","lines":["е"]},{"start":{"row":54,"column":14},"end":{"row":54,"column":15},"action":"insert","lines":["и"]}],[{"start":{"row":54,"column":15},"end":{"row":54,"column":16},"action":"insert","lines":["в"],"id":349},{"start":{"row":54,"column":16},"end":{"row":54,"column":17},"action":"insert","lines":["а"]},{"start":{"row":54,"column":17},"end":{"row":54,"column":18},"action":"insert","lines":["е"]},{"start":{"row":54,"column":18},"end":{"row":54,"column":19},"action":"insert","lines":["м"]}],[{"start":{"row":54,"column":19},"end":{"row":54,"column":20},"action":"insert","lines":[" "],"id":350},{"start":{"row":54,"column":20},"end":{"row":54,"column":21},"action":"insert","lines":["с"]},{"start":{"row":54,"column":21},"end":{"row":54,"column":22},"action":"insert","lines":["л"]},{"start":{"row":54,"column":22},"end":{"row":54,"column":23},"action":"insert","lines":["о"]},{"start":{"row":54,"column":23},"end":{"row":54,"column":24},"action":"insert","lines":["в"]},{"start":{"row":54,"column":24},"end":{"row":54,"column":25},"action":"insert","lines":["о"]}],[{"start":{"row":54,"column":25},"end":{"row":54,"column":26},"action":"insert","lines":[" "],"id":351},{"start":{"row":54,"column":26},"end":{"row":54,"column":27},"action":"insert","lines":["и"]},{"start":{"row":54,"column":27},"end":{"row":54,"column":28},"action":"insert","lines":["з"]}],[{"start":{"row":54,"column":28},"end":{"row":54,"column":29},"action":"insert","lines":[" "],"id":352},{"start":{"row":54,"column":29},"end":{"row":54,"column":30},"action":"insert","lines":["б"]},{"start":{"row":54,"column":30},"end":{"row":54,"column":31},"action":"insert","lines":["у"]},{"start":{"row":54,"column":31},"end":{"row":54,"column":32},"action":"insert","lines":["к"]},{"start":{"row":54,"column":32},"end":{"row":54,"column":33},"action":"insert","lines":["в"]}],[{"start":{"row":54,"column":20},"end":{"row":54,"column":25},"action":"remove","lines":["слово"],"id":353},{"start":{"row":54,"column":20},"end":{"row":54,"column":21},"action":"insert","lines":["п"]},{"start":{"row":54,"column":21},"end":{"row":54,"column":22},"action":"insert","lines":["а"]},{"start":{"row":54,"column":22},"end":{"row":54,"column":23},"action":"insert","lines":["р"]},{"start":{"row":54,"column":23},"end":{"row":54,"column":24},"action":"insert","lines":["о"]},{"start":{"row":54,"column":24},"end":{"row":54,"column":25},"action":"insert","lines":["л"]},{"start":{"row":54,"column":25},"end":{"row":54,"column":26},"action":"insert","lines":["ь"]}],[{"start":{"row":66,"column":8},"end":{"row":66,"column":9},"action":"remove","lines":[" "],"id":354}],[{"start":{"row":69,"column":0},"end":{"row":71,"column":24},"action":"remove","lines":["        print(password)","","        # determine hash"],"id":355},{"start":{"row":68,"column":30},"end":{"row":69,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":70,"column":0},"end":{"row":71,"column":25},"action":"remove","lines":["","        # check the match"],"id":356},{"start":{"row":69,"column":42},"end":{"row":70,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":68,"column":0},"end":{"row":68,"column":4},"action":"insert","lines":["    "],"id":357},{"start":{"row":69,"column":0},"end":{"row":69,"column":4},"action":"insert","lines":["    "]},{"start":{"row":70,"column":0},"end":{"row":70,"column":4},"action":"insert","lines":["    "]},{"start":{"row":71,"column":0},"end":{"row":71,"column":4},"action":"insert","lines":["    "]},{"start":{"row":72,"column":0},"end":{"row":72,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":62,"column":56},"end":{"row":62,"column":57},"action":"remove","lines":["2"],"id":358},{"start":{"row":62,"column":56},"end":{"row":62,"column":57},"action":"insert","lines":["3"]}],[{"start":{"row":49,"column":56},"end":{"row":49,"column":57},"action":"remove","lines":["2"],"id":359},{"start":{"row":49,"column":56},"end":{"row":49,"column":57},"action":"insert","lines":["3"]}],[{"start":{"row":62,"column":56},"end":{"row":62,"column":57},"action":"remove","lines":["3"],"id":360},{"start":{"row":62,"column":56},"end":{"row":62,"column":57},"action":"insert","lines":["4"]}],[{"start":{"row":62,"column":56},"end":{"row":62,"column":57},"action":"remove","lines":["4"],"id":361},{"start":{"row":62,"column":56},"end":{"row":62,"column":57},"action":"insert","lines":["3"]}],[{"start":{"row":36,"column":0},"end":{"row":37,"column":0},"action":"insert","lines":["",""],"id":362}],[{"start":{"row":37,"column":0},"end":{"row":37,"column":4},"action":"insert","lines":["    "],"id":363}],[{"start":{"row":37,"column":4},"end":{"row":37,"column":8},"action":"insert","lines":["    "],"id":364}],[{"start":{"row":37,"column":8},"end":{"row":37,"column":34},"action":"insert","lines":["# склеиваем пароль из букв"],"id":365}],[{"start":{"row":49,"column":0},"end":{"row":60,"column":23},"action":"remove","lines":["","for c in string.ascii_letters:     # enumeration of all 3 letters","","    # loop to iterate over the next letter","    for c1 in string.ascii_letters:","","        # склеиваем пароль из букв","        password = c + c1","        hash = crypt.crypt(password, salt)","        if hash == sys.argv[1]:","            print(password)","            sys.exit(0)"],"id":366},{"start":{"row":48,"column":0},"end":{"row":49,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":48,"column":0},"end":{"row":49,"column":0},"action":"remove","lines":["",""],"id":367}],[{"start":{"row":50,"column":65},"end":{"row":51,"column":0},"action":"remove","lines":["",""],"id":368}],[{"start":{"row":51,"column":35},"end":{"row":52,"column":0},"action":"remove","lines":["",""],"id":369}],[{"start":{"row":32,"column":65},"end":{"row":33,"column":0},"action":"remove","lines":["",""],"id":370}],[{"start":{"row":21,"column":65},"end":{"row":22,"column":0},"action":"remove","lines":["",""],"id":371}],[{"start":{"row":56,"column":27},"end":{"row":57,"column":0},"action":"insert","lines":["",""],"id":372},{"start":{"row":57,"column":0},"end":{"row":57,"column":16},"action":"insert","lines":["                "]},{"start":{"row":57,"column":16},"end":{"row":58,"column":0},"action":"insert","lines":["",""]},{"start":{"row":58,"column":0},"end":{"row":58,"column":16},"action":"insert","lines":["                "]},{"start":{"row":58,"column":16},"end":{"row":59,"column":0},"action":"insert","lines":["",""]},{"start":{"row":59,"column":0},"end":{"row":59,"column":16},"action":"insert","lines":["                "]}],[{"start":{"row":59,"column":12},"end":{"row":59,"column":16},"action":"remove","lines":["    "],"id":373},{"start":{"row":59,"column":8},"end":{"row":59,"column":12},"action":"remove","lines":["    "]},{"start":{"row":59,"column":4},"end":{"row":59,"column":8},"action":"remove","lines":["    "]},{"start":{"row":59,"column":0},"end":{"row":59,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":59,"column":0},"end":{"row":67,"column":27},"action":"insert","lines":["for c in string.ascii_letters:     # enumeration of all 3 letters","    for c1 in string.ascii_letters:","        for c2 in string.ascii_letters:","","            password = c + c1 + c2","            hash = crypt.crypt(password, salt)","            if hash == sys.argv[1]:","                print(password)","                sys.exit(0)"],"id":374}],[{"start":{"row":61,"column":39},"end":{"row":62,"column":0},"action":"insert","lines":["",""],"id":375},{"start":{"row":62,"column":0},"end":{"row":62,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":62,"column":12},"end":{"row":62,"column":43},"action":"insert","lines":["for c2 in string.ascii_letters:"],"id":376}],[{"start":{"row":62,"column":17},"end":{"row":62,"column":18},"action":"remove","lines":["2"],"id":377},{"start":{"row":62,"column":17},"end":{"row":62,"column":18},"action":"insert","lines":["3"]}],[{"start":{"row":59,"column":56},"end":{"row":59,"column":57},"action":"remove","lines":["3"],"id":378},{"start":{"row":59,"column":56},"end":{"row":59,"column":57},"action":"insert","lines":["4"]}],[{"start":{"row":64,"column":34},"end":{"row":64,"column":35},"action":"insert","lines":[" "],"id":379},{"start":{"row":64,"column":35},"end":{"row":64,"column":36},"action":"insert","lines":["+"]}],[{"start":{"row":64,"column":36},"end":{"row":64,"column":37},"action":"insert","lines":[" "],"id":380},{"start":{"row":64,"column":37},"end":{"row":64,"column":38},"action":"insert","lines":["с"]},{"start":{"row":64,"column":38},"end":{"row":64,"column":39},"action":"insert","lines":["3"]}],[{"start":{"row":57,"column":0},"end":{"row":57,"column":16},"action":"remove","lines":["                "],"id":381},{"start":{"row":58,"column":0},"end":{"row":58,"column":16},"action":"remove","lines":["                "]}],[{"start":{"row":64,"column":0},"end":{"row":64,"column":4},"action":"insert","lines":["    "],"id":386},{"start":{"row":65,"column":0},"end":{"row":65,"column":4},"action":"insert","lines":["    "]},{"start":{"row":66,"column":0},"end":{"row":66,"column":4},"action":"insert","lines":["    "]},{"start":{"row":67,"column":0},"end":{"row":67,"column":4},"action":"insert","lines":["    "]},{"start":{"row":68,"column":0},"end":{"row":68,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":37,"column":0},"end":{"row":37,"column":23},"action":"remove","lines":["        print(password)"],"id":387},{"start":{"row":36,"column":25},"end":{"row":37,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":67,"column":31},"end":{"row":68,"column":0},"action":"insert","lines":["",""],"id":388},{"start":{"row":68,"column":0},"end":{"row":68,"column":20},"action":"insert","lines":["                    "]},{"start":{"row":68,"column":20},"end":{"row":69,"column":0},"action":"insert","lines":["",""]},{"start":{"row":69,"column":0},"end":{"row":69,"column":20},"action":"insert","lines":["                    "]},{"start":{"row":69,"column":20},"end":{"row":70,"column":0},"action":"insert","lines":["",""]},{"start":{"row":70,"column":0},"end":{"row":70,"column":20},"action":"insert","lines":["                    "]}],[{"start":{"row":70,"column":16},"end":{"row":70,"column":20},"action":"remove","lines":["    "],"id":389},{"start":{"row":70,"column":12},"end":{"row":70,"column":16},"action":"remove","lines":["    "]},{"start":{"row":70,"column":8},"end":{"row":70,"column":12},"action":"remove","lines":["    "]},{"start":{"row":70,"column":4},"end":{"row":70,"column":8},"action":"remove","lines":["    "]},{"start":{"row":70,"column":0},"end":{"row":70,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":70,"column":0},"end":{"row":79,"column":31},"action":"insert","lines":["for c in string.ascii_letters:     # enumeration of all 4 letters","    for c1 in string.ascii_letters:","        for c2 in string.ascii_letters:","            for c3 in string.ascii_letters:","","                password = c + c1 + c2 + с3","                hash = crypt.crypt(password, salt)","                if hash == sys.argv[1]:","                    print(password)","                    sys.exit(0)"],"id":390}],[{"start":{"row":73,"column":43},"end":{"row":74,"column":0},"action":"insert","lines":["",""],"id":391},{"start":{"row":74,"column":0},"end":{"row":74,"column":16},"action":"insert","lines":["                "]}],[{"start":{"row":74,"column":16},"end":{"row":74,"column":47},"action":"insert","lines":["for c3 in string.ascii_letters:"],"id":392}],[{"start":{"row":74,"column":21},"end":{"row":74,"column":22},"action":"remove","lines":["3"],"id":393},{"start":{"row":74,"column":21},"end":{"row":74,"column":22},"action":"insert","lines":["4"]}],[{"start":{"row":76,"column":0},"end":{"row":76,"column":4},"action":"insert","lines":["    "],"id":394},{"start":{"row":77,"column":0},"end":{"row":77,"column":4},"action":"insert","lines":["    "]},{"start":{"row":78,"column":0},"end":{"row":78,"column":4},"action":"insert","lines":["    "]},{"start":{"row":79,"column":0},"end":{"row":79,"column":4},"action":"insert","lines":["    "]},{"start":{"row":80,"column":0},"end":{"row":80,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":76,"column":47},"end":{"row":76,"column":48},"action":"insert","lines":[" "],"id":395},{"start":{"row":76,"column":48},"end":{"row":76,"column":49},"action":"insert","lines":["+"]}],[{"start":{"row":76,"column":49},"end":{"row":76,"column":50},"action":"insert","lines":[" "],"id":396},{"start":{"row":76,"column":50},"end":{"row":76,"column":51},"action":"insert","lines":["с"]},{"start":{"row":76,"column":51},"end":{"row":76,"column":52},"action":"insert","lines":["4"]}],[{"start":{"row":68,"column":0},"end":{"row":68,"column":20},"action":"remove","lines":["                    "],"id":397},{"start":{"row":69,"column":0},"end":{"row":69,"column":20},"action":"remove","lines":["                    "]}],[{"start":{"row":63,"column":42},"end":{"row":63,"column":43},"action":"remove","lines":["3"],"id":398},{"start":{"row":63,"column":41},"end":{"row":63,"column":42},"action":"remove","lines":["с"]}],[{"start":{"row":63,"column":41},"end":{"row":63,"column":42},"action":"insert","lines":["с"],"id":399}],[{"start":{"row":63,"column":41},"end":{"row":63,"column":42},"action":"remove","lines":["с"],"id":400},{"start":{"row":63,"column":40},"end":{"row":63,"column":41},"action":"remove","lines":[" "]}],[{"start":{"row":63,"column":40},"end":{"row":63,"column":41},"action":"insert","lines":[" "],"id":401},{"start":{"row":63,"column":41},"end":{"row":63,"column":42},"action":"insert","lines":["c"]},{"start":{"row":63,"column":42},"end":{"row":63,"column":43},"action":"insert","lines":["3"]}],[{"start":{"row":76,"column":45},"end":{"row":76,"column":47},"action":"remove","lines":["с3"],"id":402},{"start":{"row":76,"column":45},"end":{"row":76,"column":46},"action":"insert","lines":["c"]},{"start":{"row":76,"column":46},"end":{"row":76,"column":47},"action":"insert","lines":["3"]}],[{"start":{"row":76,"column":50},"end":{"row":76,"column":52},"action":"remove","lines":["с4"],"id":403},{"start":{"row":76,"column":50},"end":{"row":76,"column":51},"action":"insert","lines":["c"]},{"start":{"row":76,"column":51},"end":{"row":76,"column":52},"action":"insert","lines":["4"]}],[{"start":{"row":70,"column":56},"end":{"row":70,"column":57},"action":"remove","lines":["4"],"id":404},{"start":{"row":70,"column":56},"end":{"row":70,"column":57},"action":"insert","lines":["5"]}],[{"start":{"row":80,"column":35},"end":{"row":81,"column":0},"action":"insert","lines":["",""],"id":405},{"start":{"row":81,"column":0},"end":{"row":81,"column":24},"action":"insert","lines":["                        "]},{"start":{"row":81,"column":24},"end":{"row":82,"column":0},"action":"insert","lines":["",""]},{"start":{"row":82,"column":0},"end":{"row":82,"column":24},"action":"insert","lines":["                        "]}],[{"start":{"row":82,"column":24},"end":{"row":83,"column":0},"action":"insert","lines":["",""],"id":406},{"start":{"row":83,"column":0},"end":{"row":83,"column":24},"action":"insert","lines":["                        "]}],[{"start":{"row":83,"column":20},"end":{"row":83,"column":24},"action":"remove","lines":["    "],"id":407},{"start":{"row":83,"column":16},"end":{"row":83,"column":20},"action":"remove","lines":["    "]},{"start":{"row":83,"column":12},"end":{"row":83,"column":16},"action":"remove","lines":["    "]},{"start":{"row":83,"column":8},"end":{"row":83,"column":12},"action":"remove","lines":["    "]},{"start":{"row":83,"column":4},"end":{"row":83,"column":8},"action":"remove","lines":["    "]},{"start":{"row":83,"column":0},"end":{"row":83,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":83,"column":0},"end":{"row":83,"column":11},"action":"insert","lines":["sys.exit(0)"],"id":408}],[{"start":{"row":83,"column":9},"end":{"row":83,"column":10},"action":"remove","lines":["0"],"id":409}],[{"start":{"row":83,"column":9},"end":{"row":83,"column":10},"action":"insert","lines":["1"],"id":410}],[{"start":{"row":81,"column":0},"end":{"row":81,"column":24},"action":"remove","lines":["                        "],"id":411},{"start":{"row":82,"column":0},"end":{"row":82,"column":24},"action":"remove","lines":["                        "]}]]},"timestamp":1563371374297}