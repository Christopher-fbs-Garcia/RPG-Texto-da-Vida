import random

class Countries():

    @staticmethod
    def get_countries():
        
        country = random.choice(["Brazil","Japan","Vietnam","USA","Venezuela","Haiti","Norway","Italy","Germany","France","United Kingdom",
                    "Canada","Australia","China","India","South Africa","Argentina","Mexico","Russia","Spain","Portugal","Sweden",
                    "Denmark","Netherlands","Switzerland","Belgium","Austria","New Zealand","South Korea","Singapore","Chile","Colombia",
                    "Peru","Egypt","Morocco","Turkey","Saudi Arabia","Iran","Iraq","Pakistan","Bangladesh","Indonesia","Philippines",
                    "Thailand","Malaysia","Greece","Poland","Ukraine","Cuba","Panama"])
        
        age_death = {"Brazil":76,"Japan":84,"Vietnam":73,"USA":77,"Venezuela":72,"Haiti":64,"Norway":83,"Italy":81,"Germany":81,"France":82,
                    "United Kingdom":81,"Canada":82,"Australia":83,"China":78,"India":70,"South Africa":64,"Argentina":76,"Mexico":75,"Russia":72,
                    "Spain":83,"Portugal":82,"Sweden":83,"Denmark":81,"Netherlands":82,"Switzerland":84,"Belgium":81,"Austria":81,
                    "New Zealand":82,"South Korea":83,"Singapore":84,"Chile":80,"Colombia":77,"Peru":76,"Egypt":71,"Morocco":74,
                    "Turkey":78,"Saudi Arabia":75,"Iran":76,"Iraq":70,"Pakistan":67,"Bangladesh":72,"Indonesia":71,"Philippines":70,
                    "Thailand":78,"Malaysia":76,"Greece":82,"Poland":78,"Ukraine":72,"Cuba":78,"Panama":79}
        
        death = age_death[country]

        return country, death