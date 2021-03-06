import Orange
data = Orange.data.Table('lenses')

print data.domain.features
print data.domain.class_var
for d in data[:3]:
	print d

''' lists first 5 data instances with soft perscription:'''
print 'Attributes: ', ', '.join(x.name for x in data.domain.features)
print 'Class: ', data.domain.class_var.name
print 'Data instances', len(data)

target = 'soft'
print 'Data instances with %s prescriptions: ' % target
for d in data:
	if d.get_class() == target:
		print ' '.join(['%-15s' % str(v) for v in d])