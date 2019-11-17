


class Titanic:
    def __init__(self):
        self._context = None
        self._fname = None
        self._train = None
        self._test = None
        self._testID = None


    @property
    def context(self) -> object: return self._context
    @context.setter
    def context(self, context): self._context = context


    @property
    def fname(self) -> object: return self._fname
    @fname.setter
    def fname(self, fname): self._fname = fname


    @property
    def train(self) -> object: return self._train
    @train.setter
    def train(self,train): self._train = train


    @property
    def test(self) -> object : return self._test
    @test.setter
    def test(self, test): self._test = test


    @property
    def testID(self) -> object: return self._testID
    @testID.setter
    def testID(self,testID): self._testID = testID





