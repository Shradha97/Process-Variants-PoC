# README
## Steps

* place raw data files in `data/prod-dbname` folder
* update `config/config.py` with db name 
* runAll notebooks in `src` folder
    * prep
    * featurize
    * extractVariants
* visualize the results in visualize notebook

## Folder structure

| Name | Description |
| ---- | ----------- |
| cache | Cached data files. separate by db name. **Ignored by git**|
| config | Configuration files |
| data | Input data files |
| data/prod | Production data files. **Ignored by git** |
| data/simple | Raw production data files |
| experiments | Experimental notebooks |
| scripts | Misc Python scripts e.g. to create content|
| src | Python notebooks |

