
final_array = []
for new in news:
	for value in subscriptions_data['email','state','activated_at','expires_at'].values:
		if new == value:
			final_array.append(value)

print(final_array)