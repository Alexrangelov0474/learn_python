yearly_tax = int(input())
#•	Баскетболни кецове – цената им е 40% по-малка от таксата за една година
#	Баскетболен екип – цената му е 20% по-евтина от тази на кецовете
#	Баскетболна топка – цената ѝ е 1 / 4 от цената на баскетболния екип
#	Баскетболни аксесоари – цената им е 1 / 5 от цената на баскетболната топка
sneakers = yearly_tax - (yearly_tax * 0.40)
dress = sneakers - (sneakers* 0.20)
ball = dress / 4
accessories = ball / 5

total_price = yearly_tax + sneakers + dress + ball + accessories
print(total_price)