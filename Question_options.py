#creating a dictionary of the options to the question 
sin_value = {"1":"-sinθ",
             "2":"sinx cosy + cosx siny",
             "3":"sinx cosy - cosx siny",
             "4":"2sin((x+y)/2) cos((x-y)/2)",
             "5":"2cos((x+y)/2) sin((x-y)/2)",
             "6":"sin(x+y)+sin(x-y)",
             "7":"sin(x+y)-sin(x-y)",
             "8":("2sinx cox","(2 tanx)/(1 + tan^2x)"),
             "9":"3sinx - 4sin^3x"}

cos_value = {"1":"cos(θ)",
             "2":"cosx cosy - sinx siny",
             "3":"cosx cosy + sinx siny",
             "4":"2cos((x+y)/2) cos((x-y)/2)",
             "5":"-2sin((x+y)/2) sin((x-y)/2)",
             "6":"cos(x+y)+cos(x-y)",
             "7":"cos(x+y)-cos(x-y)",
             "8":("cos^2x - sin^2x","2cos^2x - 1","1 - 2sin^2x","(1 - tan^2x)/(1 + tan^2x)"),
             "9":"4cos^3x - 3cosx"}

tan_value = {"1":"(tanx + tany)/(1-tanx tany)",
             "2":"(tanx - tany)/(1+tanx tany)",
             "3":"(2tanx)/(1-tan^2x)",
             "4":"(3tanx - tan^3x)/(1-3tan^2x)"}

cot_value = {"1":"(cotx cot-1)/(cotx+coty)",
             "2":"(cotx coty+1)/(cotx-coty)"}

#list of questions to be asked
ques_sin = ["sin(-θ)","sin(x+y)","sin(x-y)",
        "sin x + sin y", "sin x - sin y",
        "2sinx cos y","2cos x sin y","sin2x","sin3x"]

ques_cos = ["cos(-θ)","cos(x+y)","cos(x-y)",
        "cos x + cos y","cos x - cos y",
        "2cosx cos y","-2sin x sin y","cos2x","cos3x"]

ques_tan = ["tan(x+y)","tan(x-y)","tan2x","tan3x"]

ques_cot = ["cot(x+y)","cot(x-y)"]

#collects the key/option selected by the user
s,c,t,co = 0,0,0,0

def Sin(s):
  if ( s == 0): #if there is no incoming value print the options
    return sin_value
    
  else:  #once input recived return the value of the respective key
    return sin_value.get(s)

def Cos(c):
  if ( c == 0): #if there is no incoming value print the options
    return cos_value

  else:  #once input recived return the value of the respective key
    return cos_value.get(c)

def Tan(t):
  if ( t == 0): #if there is no incoming value print the options
    return tan_value

  else:  #once input recived return the value of the respective key
    return tan_value.get(t)

def Cot(co):
  if ( co == 0): #if there is no incoming value print the options
    return cot_value

  else:  #once input recived return the value of the respective key
    return cot_value.get(co)
