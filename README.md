#anatomyJSON
JSON with human anatomical terms and their properties.

Many of the anatomical terms are adapted from The Radiological Society of North America (RSNA) and The American College of Radiology (ACR) 3D Printing Registry (3DPR) version 2023-01-24. Link to current version: https://nrdrsupport.acr.org/support/solutions/articles/11000073770-3d-printing-data-dictionary
##Keys
###type
Used to describe if the anatomical term describes a area in the body or a specific structure. Terms describing a part that is too specific for a structure are deemed "comments."
-region
-subregion
-structure
-comment

###structure
Used to describe the type of structure of "comment" parts. For example, for the comment "femur," its structure is "bone."

###parent
If the part belongs to a larger region or subregion described elsewhere in the JSON, that parent is placed here. If the part can describe anatomy in more than one region, the parent is "agnostic."

###keywords
List of all substrings that might indicate the larger string would be describing this part. Currently this list includes the full anatomical name of the part, but that might be deprecated.

###exclude_keywords"
List of all substrings that indicate the larger string is not describing this part.

###laterality"
__requirement__: Indicates if the laterality should be indicated, otherwise there could be confusion as to which side of the body this part describes.
-required
-sometimes
-not applicable

__bilateral__: String or list of substring(s) that indicate the part includes both left and right sides of the anatomy.

###3DPR
Boolean describing if the part was included in the 3DPR. Will be deprecated.

###color
String of the color name or hex value that the part should be colored.

###agnostic_structure
Describes the material the part is made of, for example, "bone" or "blood vessel."
