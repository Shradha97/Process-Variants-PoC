# convert mongo json to json
# usage: mongo2json.sh <mongo json file> <json file>
# example: mongo2json.sh mongo.json json.json
# currenlty does the followig
# 1. replaces ObjectId, ISODate, Double, NumInt
# 2. It add , between } and the next {
# 3. It removes last , from the file
# 4. It adds [ and ] around the file
# 5. It cleans up the tmp files

echo $1 will be mongo cleaned json into $2
sed 's/ObjectId("\(.*\)")/"\1"/g; s/ISODate("\(.*\)")/"\1"/g; s/Double("\(.*\)")/"\1"/g; s/NumberInt(\(.*\))/"\1"/g; s/^}$/},/g' $1 > tmp

echo "[" > $2
sed '$d' tmp >> $2
echo "}" >> $2
echo "]" >> $2

rm tmp 
echo Done
