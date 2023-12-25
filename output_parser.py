from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List


class PersonIntel(BaseModel):
    summary: str = Field(discription="summary of the person")
    facts: List[str] = Field(discription="Interesting facts about the person")
    topic_of_interest: List[str] = Field(
        discription="Topics that may interest the person"
    )
    ice_breakers: List[str] = Field(
        discription="Create ice breakers to open a conversation with the person"
    )

    def to_dict(self):
        return {
            "summary": self.summary,
            "facts": self.facts,
            "topic_of_interest": self.topic_of_interest,
            "ice_breakers": self.ice_breakers,
        }


person_intel_parser: PydanticOutputParser = PydanticOutputParser(
    pydantic_object=PersonIntel
)
