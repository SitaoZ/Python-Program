from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

p1 = Point(x=10,y=30)

p2 = Point(20,30)

t = [100,200]
# make
p3 = Point._make(t)

print('p1 =',p1)
print('p2 =',p2)
print('p3 =',p3)

# asdict
d1 = p3._asdict()
print(d1)

#dict to  namedtuple
d = {'x': 11, 'y': 22}
p = Point(**d)
print('p:',p)

# replace
p3._replace(x=33)

print('p3 =',p3)

# fields
print('fields =',p3._fields)



# 添加属性

Point3D = namedtuple('Point3D', Point._fields + ('z',))

p3d = Point3D(x=1,y=2,z=3)
print('p3d:', p3d)
